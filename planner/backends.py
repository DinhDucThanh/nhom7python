from django.contrib.auth.backends import ModelBackend


class AllowInactiveModelBackend(ModelBackend):
    """
    Backend xác thực cho phép người dùng đăng nhập kể cả khi tài khoản đang bị khóa (is_active=False).
    Điều này giúp hệ thống xác thực đúng mật khẩu và điều hướng người dùng tới trang thông báo
    tài khoản bị khóa thay vì báo sai mật khẩu không chính xác.
    """
    def user_can_authenticate(self, user):
        return True
