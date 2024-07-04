from django.shortcuts import render,get_object_or_404,redirect
from .models import Thuoc
from .forms import DanhMucForm
from django.contrib import messages

def danh_muc_thuoc(request):
    items_danh_muc = Thuoc.objects.all()
    return render(request, 'danh_muc.html', {'items_danh_muc': items_danh_muc})

def them_danh_muc(request):
    if request.method == 'POST':
        ten_thuoc = request.POST['ten_thuoc']
        dvt = request.POST['dvt']
        don_gia = float(request.POST['don_gia'])
        
        item_danh_muc = Thuoc(ten_thuoc=ten_thuoc,dvt=dvt,don_gia=don_gia)
        item_danh_muc.save()

        messages.success(request,'Thuốc đã được thêm thành công!')
    return redirect('danh_muc_thuoc')

def sua_danh_muc(request, thuoc_id):
    item_danh_muc = Thuoc.objects.get(id=thuoc_id)
    
    if request.method == 'POST':
        item_danh_muc.ten_thuoc = request.POST['ten_thuoc']
        item_danh_muc.dvt = request.POST['dvt']
        item_danh_muc.don_gia = float(request.POST['don_gia'])
        
        item_danh_muc.save()

        messages.success(request,'Thuốc đã được sửa thành công!')
        return redirect('danh_muc_thuoc')
    
    return render(request,'danh_muc_thuoc',{'item_danh_muc':item_danh_muc})

def xoa_danh_muc(request, thuoc_id):
    item_danh_muc = Thuoc.objects.get(id=thuoc_id)
    item_danh_muc.delete()

    messages.success(request,'Thuốc đã được xoá thành công!')
    return redirect('danh_muc_thuoc')