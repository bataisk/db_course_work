from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginPage, sing_up_page

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login_page'),
    path('signup/', sing_up_page, name='sing_up_page'),
    path('logout/', LogoutView.as_view(), name='logout_page')
]
