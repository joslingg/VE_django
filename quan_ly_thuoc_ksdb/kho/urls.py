from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_kho, name='danh_sach_kho'),
]
