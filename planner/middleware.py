from django.shortcuts import redirect
from django.urls import reverse


class AccountLockedMiddleware:
    """
    Middleware kiểm tra người dùng đã đăng nhập nhưng tài khoản đang ở trạng thái khóa (is_active=False).
    Chặn truy cập vào các trang chức năng và tự động điều hướng sang trang /account-locked/.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_active:
            try:
                locked_url = reverse('account_locked')
                logout_url = reverse('logout')
            except Exception:
                locked_url = '/account-locked/'
                logout_url = '/logout/'

            current_path = request.path

            # Cho phép truy cập trang báo khóa, đăng xuất, static và media
            is_exempt = (
                current_path == locked_url or
                current_path.startswith(logout_url) or
                current_path.startswith('/static/') or
                current_path.startswith('/media/')
            )

            if not is_exempt:
                return redirect('account_locked')

        response = self.get_response(request)
        return response
