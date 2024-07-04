from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from benh_nhan.models import BenhNhan

class PhieuDuTru(models.Model):
    ma_benh_nhan = BenhNhan.ma_benh_nhan()
    