from django.db import models

# Create your models here.
class Thuoc(models.Model):
    ten_thuoc = models.CharField(max_length=100)
    dvt = models.CharField(max_length=50)
    don_gia = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.ten_thuoc
    