from django.urls import path
from .views import login_page, sing_up_page, logout_page

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('signup/', sing_up_page, name='sing_up_page'),
    path('logout/', logout_page, name='logout_page')
]
