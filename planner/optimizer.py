import datetime
from django.utils import timezone
from .models import Task, BusySlot, ScheduledBlock, Notification, AIInsight


class ScheduleOptimizer:
    """
    Thuật toán Tự sinh Kế hoạch Tuần (Optimization Engine)
    - Phân tích 7 ngày tới của sinh viên.
    - Trừ đi BusySlots (lịch học trường, ca làm thêm, việc cá nhân) và ScheduledBlocks đã khóa (is_locked=True).
    - Tính điểm ưu tiên cho từng task:
      Score = (Priority_Weight * 100) / max(Hours_Until_Deadline, 1) + (Remaining_Minutes / 60)
    - Chia nhỏ task thành phiên học 45-90 phút với quãng nghỉ 15 phút.
    - Xếp các phiên học vào khoảng trống theo thứ tự điểm ưu tiên cao xuống thấp.
    - Cảnh báo quá tải nếu không đủ thời gian trước deadline.
    """

    def __init__(self, user, days_ahead=7):
        self.user = user
        self.days_ahead = days_ahead
        self.tz = timezone.get_current_timezone()
        self.now = timezone.now().astimezone(self.tz)

    def optimize(self):
        # 1. Thu thập khoảng thời gian rảnh trong 7 ngày tới
        free_intervals = self._compute_free_intervals()

        # 2. Lấy các Task chưa hoàn thành
        tasks = list(Task.objects.filter(
            user=self.user,
            status__in=[Task.STATUS_TODO, Task.STATUS_IN_PROGRESS]
        ).select_related('course'))

        # Lọc ra task có thời gian cần học > 0
        active_tasks = [t for t in tasks if t.remaining_minutes > 0]

        # 3. Tính điểm ưu tiên cho từng Task
        task_scores = []
        for t in active_tasks:
            # Số giờ còn lại trước deadline
            hours_until_deadline = max((t.deadline - self.now).total_seconds() / 3600.0, 0.5)
            score = (t.priority_weight * 100.0) / max(hours_until_deadline, 1.0) + (t.remaining_minutes / 60.0)
            task_scores.append({
                'task': t,
                'score': score,
                'remaining_minutes': t.remaining_minutes,
                'deadline': t.deadline,
            })

        # Sắp xếp task theo điểm ưu tiên giảm dần
        task_scores.sort(key=lambda x: x['score'], reverse=True)

        # 4. Xóa các ScheduledBlock cũ chưa bị khóa trong 7 ngày tới
        window_end = self.now + datetime.timedelta(days=self.days_ahead)
        ScheduledBlock.objects.filter(
            task__user=self.user,
            is_locked=False,
            start_datetime__gte=self.now,
            start_datetime__lte=window_end,
            status=ScheduledBlock.STATUS_SCHEDULED,
        ).delete()

        # 5. Phân bổ các phiên học vào khoảng rảnh
        created_blocks = []
        overloaded_tasks = []

        # Sao chép các khoảng rảnh để dùng dần
        available_slots = list(free_intervals)

        for item in task_scores:
            task = item['task']
            task_rem_min = item['remaining_minutes']
            task_deadline = item['deadline']
            scheduled_min_for_task = 0

            # Chia nhỏ thời gian học: ưu tiên các block 60-90 phút, tối thiểu 45 phút
            while task_rem_min > 0:
                block_len = min(90, task_rem_min)
                if block_len < 45 and task_rem_min >= 45:
                    block_len = 45

                placed = False
                for idx, slot in enumerate(available_slots):
                    slot_start, slot_end = slot['start'], slot['end']

                    # Phiên học phải kết thúc trước deadline của task
                    if slot_start >= task_deadline:
                        continue

                    # Thời lượng slot có thể dùng (tối đa tới deadline)
                    effective_slot_end = min(slot_end, task_deadline)
                    slot_duration = int((effective_slot_end - slot_start).total_seconds() / 60)

                    if slot_duration >= 45:
                        actual_block_min = min(block_len, slot_duration)
                        block_start = slot_start
                        block_end = block_start + datetime.timedelta(minutes=actual_block_min)

                        # Tạo ScheduledBlock
                        block = ScheduledBlock.objects.create(
                            task=task,
                            start_datetime=block_start,
                            end_datetime=block_end,
                            status=ScheduledBlock.STATUS_SCHEDULED,
                            is_locked=False,
                            notes=f"Tự động xếp lịch (Điểm ưu tiên: {round(item['score'], 1)})"
                        )
                        created_blocks.append(block)

                        task_rem_min -= actual_block_min
                        scheduled_min_for_task += actual_block_min

                        # Cập nhật lại slot rảnh (chèn 15 phút nghỉ giải lao sau phiên học)
                        new_slot_start = block_end + datetime.timedelta(minutes=15)
                        if new_slot_start < slot_end:
                            available_slots[idx] = {'start': new_slot_start, 'end': slot_end}
                        else:
                            available_slots.pop(idx)

                        placed = True
                        break

                if not placed:
                    # Không còn slot trống trước deadline cho task này
                    if task_rem_min > 0:
                        overloaded_tasks.append({
                            'task': task,
                            'unassigned_minutes': task_rem_min,
                            'deadline': task_deadline
                        })
                    break

        # 6. Ghi nhận cảnh báo quá tải nếu có
        if overloaded_tasks:
            overload_msg = (
                f"Phát hiện {len(overloaded_tasks)} công việc có nguy cơ thiếu thời gian trước hạn: " +
                ", ".join([f"{ot['task'].title} (thiếu {ot['unassigned_minutes']} phút)" for ot in overloaded_tasks])
            )
            Notification.objects.create(
                user=self.user,
                title="⚠️ Cảnh báo quá tải lịch học",
                message=overload_msg,
                notification_type=Notification.TYPE_OVERLOAD_WARNING
            )
            AIInsight.objects.create(
                user=self.user,
                insight_type=AIInsight.TYPE_DEADLINE_RISK,
                title="Cảnh báo quá tải lịch học tuần",
                summary=overload_msg,
                severity=AIInsight.SEVERITY_WARNING,
                structured_data={
                    'overloaded_tasks': [
                        {'title': ot['task'].title, 'missing_minutes': ot['unassigned_minutes']}
                        for ot in overloaded_tasks
                    ]
                }
            )
        else:
            Notification.objects.create(
                user=self.user,
                title="✅ Đã tối ưu lịch học tuần",
                message=f"Đã tự động sắp xếp {len(created_blocks)} phiên học thông minh vào các khung giờ rảnh tối ưu.",
                notification_type=Notification.TYPE_SCHEDULE_GENERATED
            )

        return {
            'status': 'success',
            'created_blocks_count': len(created_blocks),
            'overloaded_tasks_count': len(overloaded_tasks),
            'overloaded_tasks': [
                {'title': ot['task'].title, 'unassigned_minutes': ot['unassigned_minutes']}
                for ot in overloaded_tasks
            ]
        }

    def _compute_free_intervals(self):
        """
        Tính toán danh sách các khoảng thời gian trống theo từng ngày trong 7 ngày tới.
        Khung giờ học mỗi ngày: user.study_start_hour -> user.study_end_hour.
        Trừ đi BusySlots và ScheduledBlocks đã khóa.
        """
        study_start = self.user.study_start_hour
        study_end = self.user.study_end_hour

        # Lấy BusySlots lặp lại và cố định
        busy_slots = list(BusySlot.objects.filter(user=self.user))

        # Lấy các ScheduledBlock đã khóa (is_locked=True)
        locked_blocks = list(ScheduledBlock.objects.filter(
            task__user=self.user,
            is_locked=True,
            start_datetime__gte=self.now,
            start_datetime__lte=self.now + datetime.timedelta(days=self.days_ahead)
        ))

        free_intervals = []

        for d in range(self.days_ahead):
            current_day_date = (self.now + datetime.timedelta(days=d)).date()

            # Giờ bắt đầu và kết thúc của ngày học
            day_study_start = datetime.datetime.combine(current_day_date, study_start, tzinfo=self.tz)
            day_study_end = datetime.datetime.combine(current_day_date, study_end, tzinfo=self.tz)

            # Nếu là ngày hôm nay và đã qua giờ bắt đầu học, dịch giờ bắt đầu lên thời điểm hiện tại
            if current_day_date == self.now.date() and self.now > day_study_start:
                day_study_start = self.now + datetime.timedelta(minutes=10) # 10p đệm

            if day_study_start >= day_study_end:
                continue

            # Thu thập các khoảng bận trong ngày này
            blocked_spans = []

            # 1. BusySlots
            weekday = current_day_date.weekday()
            for bs in busy_slots:
                if bs.is_recurring and bs.day_of_week == weekday:
                    b_start = datetime.datetime.combine(current_day_date, bs.start_time, tzinfo=self.tz)
                    b_end = datetime.datetime.combine(current_day_date, bs.end_time, tzinfo=self.tz)
                    blocked_spans.append((b_start, b_end))
                elif not bs.is_recurring and bs.specific_date == current_day_date:
                    b_start = datetime.datetime.combine(current_day_date, bs.start_time, tzinfo=self.tz)
                    b_end = datetime.datetime.combine(current_day_date, bs.end_time, tzinfo=self.tz)
                    blocked_spans.append((b_start, b_end))

            # 2. Locked ScheduledBlocks
            for lb in locked_blocks:
                if lb.start_datetime.date() == current_day_date:
                    blocked_spans.append((lb.start_datetime, lb.end_datetime))

            # Hợp nhất các khoảng bận trùng lặp
            merged_busy = self._merge_intervals(blocked_spans)

            # Cắt các khoảng rảnh từ [day_study_start, day_study_end]
            curr_cursor = day_study_start
            for b_start, b_end in merged_busy:
                # Bỏ qua nếu bận nằm hoàn toàn ngoài khung giờ học
                if b_end <= curr_cursor or b_start >= day_study_end:
                    continue

                if b_start > curr_cursor:
                    seg_start = max(curr_cursor, day_study_start)
                    seg_end = min(b_start, day_study_end)
                    if (seg_end - seg_start).total_seconds() >= 45 * 60: # ít nhất 45 phút
                        free_intervals.append({'start': seg_start, 'end': seg_end})

                curr_cursor = max(curr_cursor, b_end)

            if curr_cursor < day_study_end:
                seg_start = max(curr_cursor, day_study_start)
                seg_end = day_study_end
                if (seg_end - seg_start).total_seconds() >= 45 * 60:
                    free_intervals.append({'start': seg_start, 'end': seg_end})

        return free_intervals

    def _merge_intervals(self, intervals):
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged = [sorted_intervals[0]]
        for current in sorted_intervals[1:]:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = current
            if curr_start <= prev_end:
                merged[-1] = (prev_start, max(prev_end, curr_end))
            else:
                merged.append(current)
        return merged
