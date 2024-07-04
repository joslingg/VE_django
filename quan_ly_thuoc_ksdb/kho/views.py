from django.shortcuts import render,redirect,get_object_or_404
from .models import Kho
from .forms import KhoForm
from danh_muc_thuoc.models import Thuoc
from django.contrib import messages
from django.http import JsonResponse

def danh_sach_kho(request):
    items_thuoc = Kho.objects.all()
    items_danh_muc = Thuoc.objects.all()
    return render(request,'kho.html',{'items_thuoc':items_thuoc, 'items_danh_muc':items_danh_muc})
    

def nhap_thuoc(request):
    if request.method == "POST":
        ngay_nhap = request.POST.get('ngay_nhap')
        ten_thuoc = request.POST.get('thuoc')
        dvt = request.POST.get('dvt')
        don_gia = request.POST.get('don_gia')
        so_luong_nhap = int(request.POST.get('so_luong_nhap'))
        
        
        item_thuoc = Kho(ngay_nhap=ngay_nhap,ten_thuoc=ten_thuoc,dvt=dvt,don_gia=don_gia,so_luong_nhap=so_luong_nhap)
        item_thuoc.save()
        
        messages.success(request,'Thuốc đã được nhập thành công!')
        return redirect('danh_sach_kho.html')
    items_danh_muc = Thuoc.objects.all()
    return render(request, 'nhap_thuoc', {'items_danh_muc': items_danh_muc})

def lay_tt_thuoc(request, thuoc_id):
    item_danh_muc = Thuoc.objects.get(id=thuoc_id)
    data = {
        'dvt': item_danh_muc.dvt,
        'don_gia': item_danh_muc.don_gia,
    }
    return JsonResponse(data)
        
        