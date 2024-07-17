from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import PhieuNhap,ctPhieuNhap
from danh_muc_thuoc.models import Thuoc
from kho.models import Kho
from django.contrib import messages
from datetime import datetime
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Count, IntegerField
from .forms import NhapThuocForm

def danh_sach_phieu_nhap(request):
    items_danh_muc = Thuoc.objects.all()
    items_ct_phieu_nhap = ctPhieuNhap.objects.none()  # Khởi tạo biến rỗng
    so_phieu_nhap = request.GET.get('filter_so_phieu_nhap')
    print(f"Received so_phieu_nhap: {so_phieu_nhap}")  # In giá trị để kiểm tra
    months = range(1,13)
    current_year = datetime.now().year
    years = range(2023, current_year+1)
    thang = request.GET.get('thang')
    nam = request.GET.get('nam')
    items_phieu_nhap = PhieuNhap.objects.all()
    
    form = NhapThuocForm()
    
    if thang and nam:
        items_phieu_nhap = PhieuNhap.objects.annotate(
            ngay_nhap_thang=ExtractMonth('ngay_nhap', output_field=IntegerField()),
            ngay_nhap_nam=ExtractYear('ngay_nhap')
        ).filter(ngay_nhap_thang=thang, ngay_nhap_nam=nam)
            
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        phieu_list = list(items_phieu_nhap.values('id', 'so_phieu_nhap'))
        return JsonResponse({'phieu_list': phieu_list})
    
    if so_phieu_nhap:
        # Lọc chi tiết phiếu nhập dựa trên số phiếu nhập
        phieu_nhap = get_object_or_404(PhieuNhap, so_phieu_nhap=so_phieu_nhap)
        items_ct_phieu_nhap = ctPhieuNhap.objects.filter(phieu_nhap=phieu_nhap)
    
    return render(request, 'phieu_nhap_kho.html', {
        'items_danh_muc':items_danh_muc,
        'items_ct_phieu_nhap':items_ct_phieu_nhap,
        'months':months, 'years':years,
        'items_phieu_nhap':items_phieu_nhap,
        'form':form
        })

    
def nhap_thuoc(request):
    if request.method == "POST":
        ngay_nhap = request.POST.get('ngay_nhap')
        so_phieu_nhap = request.POST.get('so_phieu_nhap')

        #Tạo phiếu nhập mới
        item_phieu_nhap = PhieuNhap(so_phieu_nhap=so_phieu_nhap, ngay_nhap=ngay_nhap)
        item_phieu_nhap.save()
        
        # Lặp qua từng loại thuốc
        thuoc_ids = request.POST.getlist('ten_thuoc')
        so_luong_nhaps = request.POST.getlist('so_luong_nhap')

        for thuoc_id, so_luong_nhap in zip(thuoc_ids, so_luong_nhaps):
            item_danh_muc = get_object_or_404(Thuoc, id=thuoc_id)
            so_luong_nhap = int(so_luong_nhap)
        
            try:
                item_thuoc = Kho.objects.get(thuoc=item_danh_muc)
                # Nếu tồn tại, cập nhật số lượng nhập, số lượng tồn
                item_thuoc.so_luong_nhap += so_luong_nhap
                item_thuoc.so_luong_ton += so_luong_nhap - item_thuoc.so_luong_xuat
                item_thuoc.ngay_nhap = ngay_nhap
                item_thuoc.save()
            except Kho.DoesNotExist:
                # Nếu không tồn tại, tạo mới
                so_luong_xuat = 0
                so_luong_ton = so_luong_nhap - so_luong_xuat
                item_thuoc = Kho(thuoc=item_danh_muc, so_luong_nhap=so_luong_nhap, so_luong_xuat=so_luong_xuat, so_luong_ton=so_luong_ton)
                item_thuoc.save()

            item_ct_phieu_nhap = ctPhieuNhap(phieu_nhap=item_phieu_nhap, thuoc=item_danh_muc, so_luong_nhap=so_luong_nhap)
            item_ct_phieu_nhap.save()

        messages.success(request, 'Thuốc đã được nhập thành công!')
        return redirect('danh_sach_phieu_nhap')

    items_danh_muc = Thuoc.objects.all()
    return render(request, 'danh_sach_phieu_nhap', {'items_danh_muc': items_danh_muc})

def sua_ct_phieu_nhap(request, id):
    ct_phieu_nhap = get_object_or_404(ctPhieuNhap, id=id)
    item_kho = get_object_or_404(Kho, thuoc=ct_phieu_nhap.thuoc)
    
    if request.method == 'POST':
        new_so_luong_nhap = int(request.POST.get('so_luong_nhap'))
        
        item_kho.so_luong_ton -= ct_phieu_nhap.so_luong_nhap
        
        ct_phieu_nhap.so_luong_nhap = new_so_luong_nhap
        ct_phieu_nhap.save()
        
        item_kho.so_luong_ton += new_so_luong_nhap
        item_kho.save()
        messages.success(request,'Sửa phiếu nhập thành công!')
        items_danh_muc = Thuoc.objects.all()
        
        return redirect('danh_sach_phieu_nhap')
    
        
        

def xoa_ct_phieu_nhap(request,id):
    ct_phieu_nhap = get_object_or_404(ctPhieuNhap,id=id)
    item_kho = get_object_or_404(Kho, thuoc=ct_phieu_nhap.thuoc)
    
    if request == 'POST':
        item_kho.so_luong_ton -= ct_phieu_nhap.so_luong_nhap
        item_kho.save()
        ct_phieu_nhap.delete()
        messages.success(request,'Xoá thuốc trong phiếu nhập thành công')
        
        return redirect('danh_sach_phieu_nhap')


        
        
