# forms.py
from django import forms
from .models import BenhNhan

class BenhNhanForm(forms.ModelForm):
    class Meta:
        model = BenhNhan
        fields = ['ma_benh_nhan', 'ho_ten', 'ngay_sinh', 'khoa']

class TimKiemBenhNhanForm(forms.Form):
    ma_benh_nhan = forms.CharField(required=False, max_length=8, label='Mã bệnh nhân')
    ho_ten = forms.CharField(required=False, max_length=255, label='Họ tên')
    ngay_sinh = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Ngày sinh')
    khoa = forms.ChoiceField(required=False, choices=[('', '---')] + BenhNhan.khoa_choices, label='Khoa')
