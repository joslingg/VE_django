# Generated by Django 4.2.13 on 2024-07-03 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kho', '0002_alter_kho_ten_thuoc_delete_danhmuc'),
        ('danh_muc_thuoc', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DanhMuc',
            new_name='Thuoc',
        ),
    ]
