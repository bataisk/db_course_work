from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from .views import LoginPage, sing_up_page

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login_page'),
    path('signup/', sing_up_page, name='sing_up_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
