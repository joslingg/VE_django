# Generated by Django 4.2.13 on 2024-07-03 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kho', '0002_alter_kho_ten_thuoc_delete_danhmuc'),
    ]

    operations = [
        migrations.AddField(
            model_name='kho',
            name='ngay_nhap',
            field=models.DateField(default=datetime.date.today),
        ),
    ]