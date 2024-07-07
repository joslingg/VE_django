from django import forms
from .models import Kho
from danh_muc_thuoc.models import Thuoc

class KhoForm(forms.ModelForm):
    
    class Meta:
        model = Kho
        fields = ['thuoc']