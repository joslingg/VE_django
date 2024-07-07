from django.db import models
from danh_muc_thuoc.models import Thuoc
from datetime import date

# Create your models here.
class Kho(models.Model):
    thuoc = models.ForeignKey(Thuoc, on_delete=models.CASCADE)
    so_luong_nhap = models.PositiveIntegerField()
    so_luong_xuat = models.PositiveIntegerField()
    so_luong_ton = models.PositiveIntegerField()
    
