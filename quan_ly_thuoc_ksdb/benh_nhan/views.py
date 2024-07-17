# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import BenhNhan
from .forms import BenhNhanForm

def danh_sach_benh_nhan(request):
    # Lấy các tham số từ query string để tìm kiếm
    ma_benh_nhan = request.GET.get('ma_benh_nhan', '')
    ho_ten = request.GET.get('ho_ten', '')
    ngay_sinh = request.GET.get('ngay_sinh', '')
    khoa = request.GET.get('khoa', '')

    # Lọc dữ liệu theo các tham số tìm kiếm nếu có
    form = BenhNhanForm()
    benh_nhans = BenhNhan.objects.all()
    if ma_benh_nhan:
        benh_nhans = benh_nhans.filter(ma_benh_nhan__icontains=ma_benh_nhan)
    if ho_ten:
        benh_nhans = benh_nhans.filter(ho_ten__icontains=ho_ten)
    if ngay_sinh:
        benh_nhans = benh_nhans.filter(ngay_sinh=ngay_sinh)
    if khoa:
        benh_nhans = benh_nhans.filter(khoa=khoa)

    return render(request, 'benh_nhan.html', {'benh_nhans': benh_nhans, 'form' : form})

def them_benh_nhan(request):
    if request.method == 'POST':
        form = BenhNhanForm(request.POST)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                # Render partial template for modal
                html = render_to_string('modal_success.html', {'form': form})
                return JsonResponse({'success': True, 'html': html})
            return redirect('danh_sach_benh_nhan')
        else:
            if request.is_ajax():
                # Render partial template with form errors
                html = render_to_string('modal_form.html', {'form': form})
                return JsonResponse({'success': False, 'html': html})
    else:
        form = BenhNhanForm()

    if request.is_ajax():
        html = render_to_string('modal_form.html', {'form': form})
        return JsonResponse({'html': html})

    return render(request, 'them_benh_nhan.html', {'form': form})

def sua_benh_nhan(request, id):
    benh_nhan = get_object_or_404(BenhNhan, id=id)
    if request.method == 'POST':
        form = BenhNhanForm(request.POST, instance=benh_nhan)
        if form.is_valid():
            form.save()
    else:
        form = BenhNhanForm(instance=benh_nhan)
    return redirect('danh_sach_benh_nhan')

def xoa_benh_nhan(request, id):
    benh_nhan = get_object_or_404(BenhNhan, id=id)
    if request.method == 'POST':
        benh_nhan.delete()
        return redirect('danh_sach_benh_nhan')
    

