from django.urls import path
from .views import discover_page

urlpatterns = [
    path('movie/', discover_page, name='discover_movie'),
    path('show/', discover_page, name='discover_show'),
    path('title/', discover_page, name='discover_title')
]
