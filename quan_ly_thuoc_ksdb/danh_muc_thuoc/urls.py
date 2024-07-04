from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_muc_thuoc, name='danh_muc_thuoc'),
    path('them_danh_muc/', views.them_danh_muc, name='them_danh_muc'),
    path('sua_danh_muc/<int:id>', views.sua_danh_muc, name='sua_danh_muc'),
]