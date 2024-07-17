from django import forms
from .models import PhieuNhap, ctPhieuNhap
from danh_muc_thuoc.models import Thuoc

class NhapThuocForm(forms.ModelForm):
    class Meta:
        model = ctPhieuNhap
        fields = ['phieu_nhap', 'thuoc', 'so_luong_nhap']

    def clean_so_luong_nhap(self):
        data = self.cleaned_data['so_luong_nhap']
        if data <= 0:
            raise forms.ValidationError("Số lượng nhập phải lớn hơn 0.")
        return data
