# Generated by Django 4.2.13 on 2024-07-03 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DanhMuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_thuoc', models.CharField(max_length=100)),
                ('dvt', models.CharField(max_length=50)),
                ('don_gia', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Kho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ton_dau', models.DecimalField(decimal_places=0, max_digits=5)),
                ('so_luong_nhap', models.DecimalField(decimal_places=0, max_digits=5)),
                ('so_luong_xuat', models.DecimalField(decimal_places=0, max_digits=5)),
                ('ton_cuoi', models.DecimalField(decimal_places=0, max_digits=5)),
                ('thang', models.IntegerField(choices=[(1, 'Tháng 1'), (2, 'Tháng 2'), (3, 'Tháng 3'), (4, 'Tháng 4'), (5, 'Tháng 5'), (6, 'Tháng 6'), (7, 'Tháng 7'), (8, 'Tháng 8'), (9, 'Tháng 9'), (10, 'Tháng 10'), (11, 'Tháng 11'), (12, 'Tháng 12')])),
                ('nam', models.IntegerField()),
                ('ten_thuoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kho.danhmuc')),
            ],
        ),
    ]
