from django.db import models
from danh_muc_thuoc.models import Thuoc
from datetime import date

# Create your models here.
class Kho(models.Model):
    ngay_nhap = models.DateField()
    ten_thuoc = models.ForeignKey(Thuoc, on_delete=models.CASCADE)
    dvt = models.CharField(max_length=20, blank=True, null=True)
    don_gia = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ton_cuoi = models.PositiveIntegerField()
    so_luong_nhap = models.PositiveIntegerField()
    so_luong_xuat = models.PositiveIntegerField()
    
