from django.db import models
from danh_muc_thuoc.models import Thuoc
from datetime import date

# Create your models here.
class Kho(models.Model):
    ngay_nhap = models.DateField(default=date.today)
    ten_thuoc = models.ForeignKey(Thuoc, on_delete=models.CASCADE)
    dvt = models.CharField(max_length=50, blank=True, null=True)
    don_gia = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ton_dau = models.DecimalField(max_digits=5,decimal_places=0)
    so_luong_nhap = models.DecimalField(max_digits=5, decimal_places=0)
    so_luong_xuat = models.DecimalField(max_digits=5, decimal_places=0)
    ton_cuoi = models.DecimalField(max_digits=5,decimal_places=0)
    thang_choices = [
        (1, 'Tháng 1'), (2, 'Tháng 2'), (3, 'Tháng 3'),
        (4, 'Tháng 4'), (5, 'Tháng 5'), (6, 'Tháng 6'),
        (7, 'Tháng 7'), (8, 'Tháng 8'), (9, 'Tháng 9'),
        (10, 'Tháng 10'), (11, 'Tháng 11'), (12, 'Tháng 12'),
    ]
    thang = models.IntegerField(choices=thang_choices)
    nam = models.IntegerField()
    
    def save(self, *args, **kwargs):
        # Tính tồn đầu dựa trên tồn cuối của tháng trước đó
        if self.ton_dau is None:
            self.ton_dau = self.tinh_ton_dau(self.ten_thuoc, self.thang, self.nam)
        self.ton_cuoi = self.ton_dau + self.so_luong_nhap - self.so_luong_xuat
        super(Kho, self).save(*args, **kwargs)
        
    @classmethod
    def tinh_ton_dau(cls, ten_thuoc, thang, nam):
        # Tìm tồn cuối của tháng trước
        if thang == 1:
            thang_truoc = 12
            nam_truoc = nam - 1
        else:
            thang_truoc = thang - 1
            nam_truoc = nam

        ton_truoc = cls.objects.filter(
            ten_thuoc=ten_thuoc,
            thang=thang_truoc,
            nam=nam_truoc
        ).order_by('-nam', '-thang').first()

        if ton_truoc:
            return ton_truoc.ton_cuoi
        else:
            return 0

    def __str__(self):
        return f'{self.ten_thuoc} - Tháng {self.thang}/{self.nam}'