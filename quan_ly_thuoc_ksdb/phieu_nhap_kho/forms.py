from django import forms
from .models import PhieuNhap, ctPhieuNhap
from danh_muc_thuoc.models import Thuoc

class NhapThuocForm(forms.Form):
    model = PhieuNhap
    fields = ['thang', 'nam', 'so_phieu_nhap']
    ngay_nhap = forms.DateField(label='Ngày nhập', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    so_phieu_nhap = forms.CharField(label='Số phiếu nhập', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    ten_thuoc = forms.ModelChoiceField(queryset=Thuoc.objects.all(), label='Tên thuốc', empty_label='--- Chọn thuốc ---', widget=forms.Select(attrs={'class': 'form-control'}))
    so_luong_nhap = forms.IntegerField(label='Số lượng nhập', widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'min': 0}))

    def clean_so_luong_nhap(self):
        data = self.cleaned_data['so_luong_nhap']
        if data <= 0:
            raise forms.ValidationError("Số lượng nhập phải lớn hơn 0.")
        return data
