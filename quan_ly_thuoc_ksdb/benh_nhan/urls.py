from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('benh_nhan/',views.danh_sach_benh_nhan,name='danh_sach_benh_nhan'),
    path('them_benh_nhan/',views.them_benh_nhan, name='them_benh_nhan'),
    path('sua_benh_nhan/<int:id>/',views.sua_benh_nhan, name='sua_benh_nhan'),
    path('xoa_benh_nhan/<int:id>/',views.xoa_benh_nhan, name='xoa_benh_nhan'),
]
