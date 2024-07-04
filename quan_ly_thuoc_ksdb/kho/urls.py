from django.urls import path
from . import views

urlpatterns = [
    path('', views.kho_thuoc, name='kho'),
    path('nhap_thuoc/', views.nhap_thuoc, name='nhap_thuoc'),
    path('lay_thuoc/', views.lay_thuoc, name='lay_thuoc'),
]
