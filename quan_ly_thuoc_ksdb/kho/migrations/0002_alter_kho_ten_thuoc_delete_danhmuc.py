# Generated by Django 4.2.13 on 2024-07-03 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('danh_muc_thuoc', '0001_initial'),
        ('kho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kho',
            name='ten_thuoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danh_muc_thuoc.danhmuc'),
        ),
        migrations.DeleteModel(
            name='DanhMuc',
        ),
    ]