from django import forms
from .models import Kho
from danh_muc_thuoc.models import Thuoc

class KhoForm(forms.ModelForm):
    thuoc = forms.ModelChoiceField(
        queryset=Thuoc.objects.all(),
        label='Tên thuốc',
        empty_label="--- Chọn thuốc ---",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Kho
        fields = ['ngay_nhap','ten_thuoc','so_luong_nhap','thang','nam']
        
        widgets = {
            'thang': forms.Select(choices=[(i, f'Tháng {i}') for i in range(1, 13)]),
            'nam': forms.Select(choices=[(year, year) for year in range(2020, 2031)]),  # Update years as needed
        }