# Generated by Django 5.0.6 on 2024-07-07 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kho', '0006_rename_ton_cuoi_kho_so_luong_ton_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kho',
            name='ngay_nhap',
        ),
    ]
