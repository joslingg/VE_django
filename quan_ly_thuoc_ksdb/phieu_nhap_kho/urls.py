from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_phieu_nhap, name='danh_sach_phieu_nhap'),
    path('nhap_thuoc/', views.nhap_thuoc, name='nhap_thuoc'),
    path('sua_ct_phieu_nhap/<int:id>/', views.sua_ct_phieu_nhap, name='sua_ct_phieu_nhap'),
    path('xoa_ct_phieu_nhap/<int:id>/',views.xoa_ct_phieu_nhap,name='xoa_ct_phieu_nhap'),
]