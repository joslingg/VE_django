from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_phieu_nhap, name='danh_sach_phieu_nhap'),
    path('them_phieu_nhap/', views.them_phieu_nhap, name='them_phieu_nhap'),
    path('xem_phieu_nhap/<int:id>/', views.xem_phieu_nhap, name='xem_phieu_nhap'),
    path('sua_phieu_nhap/<int:id>/', views.sua_phieu_nhap, name='sua_phieu_nhap'),
    path('xoa_phieu_nhap/<int:id>/', views.xoa_phieu_nhap, name='xoa_phieu_nhap'),
]