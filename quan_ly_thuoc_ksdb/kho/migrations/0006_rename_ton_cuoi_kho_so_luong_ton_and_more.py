# Generated by Django 5.0.6 on 2024-07-05 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kho', '0005_remove_kho_nam_remove_kho_thang_remove_kho_ton_dau_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kho',
            old_name='ton_cuoi',
            new_name='so_luong_ton',
        ),
        migrations.RenameField(
            model_name='kho',
            old_name='ten_thuoc',
            new_name='thuoc',
        ),
        migrations.RemoveField(
            model_name='kho',
            name='don_gia',
        ),
        migrations.RemoveField(
            model_name='kho',
            name='dvt',
        ),
    ]