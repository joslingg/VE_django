from django import forms
from .models import BenhNhan

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
        if BenhNhan.objects.filter(ma_benh_nhan=ma_benh_nhan).exists():
            raise forms.ValidationError("Mã bệnh nhân đã tồn tại.")
        return ma_benh_nhan

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if self.errors.get(name):
                field.widget.attrs.update({'class': 'form-control is-invalid'})

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
