from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_kho, name='danh_sach_kho'),
    path('nhap_thuoc/', views.nhap_thuoc, name='nhap_thuoc'),
    path('lay_tt_thuoc/<int:thuoc_id>', views.lay_tt_thuoc, name='lay_tt_thuoc'),
]
