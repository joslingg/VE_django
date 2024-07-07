from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_phieu_nhap, name='danh_sach_phieu_nhap'),
    path('nhap_thuoc/', views.nhap_thuoc, name='nhap_thuoc'),
]