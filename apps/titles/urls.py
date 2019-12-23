from django.urls import path
from .views import title_page

urlpatterns = [
    path('<int:title_id>', title_page)
]
