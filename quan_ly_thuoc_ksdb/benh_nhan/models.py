from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class BenhNhan(models.Model):
    khoa_choices = [
        ('Khoa Khám Bệnh','Khoa Khám Bệnh'),
        ('Khoa Ngoại','Khoa Ngoại'),
        ('Khoa Nội Nhiễm','Khoa Nội Nhiễm'),
        ('Khoa Chăm Sóc Giảm Nhẹ','Khoa Chăm Sóc Giảm Nhẹ'),
        ('Khoa Dưỡng Lão Nam','Khoa Dưỡng Lão Nam'),
        ('Khoa Dưỡng Lão Nữ','Khoa  Dưỡng Lão Nữ'),
        ('Khoa Khám Bệnh Nội Viện','Khoa Khám Bệnh Nội Viện'),
        ('Khoa Tâm Thần','Khoa Tâm Thần'),
    ]
     
    ma_benh_nhan = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex='^\d{8}$',
                message='Mã bệnh nhân phải gồm 8 chữ số.',
            ),
        ],
    )
    ho_ten = models.CharField(max_length=255)
    ngay_sinh = models.DateField()
    khoa = models.CharField(max_length=100,choices=khoa_choices)
     
    def __str__(self):
        return f"{self.ma_benh_nhan} - {self.ho_ten}"
