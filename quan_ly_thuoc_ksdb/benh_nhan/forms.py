from django import forms
from .models import BenhNhan
from django.core.exceptions import ValidationError

class BenhNhanForm(forms.ModelForm):
    class Meta:
        model = BenhNhan
        fields = ['ma_benh_nhan', 'ho_ten', 'ngay_sinh', 'khoa']
        labels = {
            'ma_benh_nhan': 'Mã bệnh nhân',
            'ho_ten': 'Họ tên',
            'ngay_sinh': 'Ngày sinh',
            'khoa': 'Khoa',
        }
        widgets = {
            'ma_benh_nhan': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 8}),
            'ho_ten': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'ngay_sinh': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'khoa': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_ma_benh_nhan(self):
        ma_benh_nhan = self.cleaned_data.get('ma_benh_nhan')
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # Đang cập nhật bệnh nhân hiện có
            if BenhNhan.objects.exclude(pk=instance.pk).filter(ma_benh_nhan=ma_benh_nhan).exists():
                raise ValidationError("Mã bệnh nhân này đã tồn tại trong hệ thống.")
        else:
            # Đang tạo bệnh nhân mới
            if BenhNhan.objects.filter(ma_benh_nhan=ma_benh_nhan).exists():
                raise ValidationError("Mã bệnh nhân này đã tồn tại trong hệ thống.")
        return ma_benh_nhan

class TimKiemBenhNhanForm(forms.Form):
    ma_benh_nhan = forms.CharField(
        required=False, 
        max_length=8, 
        label='Mã bệnh nhân', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ho_ten = forms.CharField(
        required=False, 
        max_length=255, 
        label='Họ tên', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ngay_sinh = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
        label='Ngày sinh'
    )
    khoa = forms.ChoiceField(
        required=False, 
        choices=[('', '---')] + BenhNhan.khoa_choices, 
        label='Khoa', 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
