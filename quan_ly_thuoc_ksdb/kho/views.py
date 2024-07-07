from django.shortcuts import render,redirect,get_object_or_404
from .models import Kho
from danh_muc_thuoc.models import Thuoc
from django.contrib import messages

def danh_sach_kho(request):
    items_thuoc = Kho.objects.all()
    items_danh_muc = Thuoc.objects.all()
    return render(request,'kho.html',{'items_thuoc':items_thuoc, 'items_danh_muc':items_danh_muc})

        
        