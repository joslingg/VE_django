from django import forms
from .models import Thuoc

class DanhMucForm(forms.ModelForm):
    class Meta:
        model = Thuoc
        fields = ['ten_thuoc','dvt','don_gia']