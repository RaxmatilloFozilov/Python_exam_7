from django.urls import path
from .views import (
    RegisterView,
    insert_email_4_change_password, reset_password,
    change_password, confirm_email,
    login, LogoutView
)


urlpatterns = [
    path('registers/', RegisterView.as_view(), name='signup'),
    path('password_reset/email/', insert_email_4_change_password, name='password_reset'),
    path('password_reset/', reset_password, name='reset_password'),
    path('password_change/', change_password, name='change_password'),
    path('confirm_email/', confirm_email, name='confirm_email'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
