from django.db import models
from danh_muc_thuoc.models import Thuoc
from datetime import date

# Create your models here.
class PhieuNhap(models.Model):
    so_phieu_nhap = models.CharField(max_length=20, blank=True)
    ngay_nhap = models.DateField()

class ctPhieuNhap(models.Model):
    phieu_nhap = models.ForeignKey(PhieuNhap, on_delete=models.CASCADE, default=1)
    thuoc = models.ForeignKey(Thuoc, on_delete=models.CASCADE)
    so_luong_nhap = models.PositiveIntegerField()
