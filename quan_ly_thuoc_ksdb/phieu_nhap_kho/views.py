from django.shortcuts import render,redirect,get_object_or_404
from .models import PhieuNhap,ctPhieuNhap
from danh_muc_thuoc.models import Thuoc
from kho.models import Kho
from django.contrib import messages
from datetime import datetime
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Count, IntegerField

def danh_sach_phieu_nhap(request):
    if request.method == "GET":
        months = range(1,13)
        current_year = datetime.now().year
        years = range(2023, current_year+1)
        thang = request.GET.get('thang')
        nam = request.GET.get('nam')
        items_phieu_nhap = PhieuNhap.objects.all()
        if thang and nam:
            items_phieu_nhap = PhieuNhap.objects.annotate(
                ngay_nhap_thang=ExtractMonth('ngay_nhap', output_field=IntegerField()),
                ngay_nhap_nam=ExtractYear('ngay_nhap')
            ).filter(ngay_nhap_thang=thang, ngay_nhap_nam=nam)
        return render(request, 'phieu_nhap_kho.html', {'months':months, 'years':years, 'items_phieu_nhap':items_phieu_nhap})

def danh_sach_ct_phieu_nhap(request):
    items_ct_phieu_nhap = ctPhieuNhap.objects.all()
    return render(request, {'items_ct_phieu_nhap':items_ct_phieu_nhap})
    

def nhap_thuoc(request):
    if request.method == "POST":
        ngay_nhap = request.POST.get('ngay_nhap')
        thuoc_id = request.POST.get('ten_thuoc')
        item_danh_muc = get_object_or_404(Thuoc, id=thuoc_id)
        so_luong_nhap = int(request.POST.get('so_luong_nhap'))
        # Kiểm tra xem sản phẩm đã tồn tại trong kho hay chưa
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
            item_thuoc = Kho(ngay_nhap=ngay_nhap, thuoc=item_danh_muc, so_luong_nhap=so_luong_nhap, so_luong_xuat=so_luong_xuat, so_luong_ton=so_luong_ton)
            item_thuoc.save()
        
        messages.success(request,'Thuốc đã được nhập thành công!')
        return redirect('/danh_sach_kho')
    items_thuoc = Kho.objects.all()
    items_danh_muc = Thuoc.objects.all()
    return render(request, 'nhap_thuoc', {'items_thuoc':items_thuoc,'items_danh_muc': items_danh_muc})

        
        
