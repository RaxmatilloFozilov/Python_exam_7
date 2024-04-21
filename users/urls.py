from django.urls import path

from users.views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
]




# router.register(r'change_password', ChangePasswordView)
# router.register(r'reset_password', ResetPasswordView)