from django.shortcuts import render,redirect
from .models import Kho
from .forms import KhoForm
from danh_muc_thuoc.models import Thuoc
from django.http import JsonResponse

def kho_thuoc(request):
    if request.method == 'GET':
        selected_thang = request.GET.get('thang')
        selected_nam = request.GET.get('nam')
        
        thuoc = Kho.objects.filter(thang=selected_thang, nam=selected_nam)
        
        return render(request, 'kho.html', {'kho': kho_thuoc, 'selected_thang': selected_thang, 'selected_nam': selected_nam})

    return render(request, 'kho.html', {'kho': None, 'selected_thang': None, 'selected_nam': None})

def nhap_thuoc(request):
    if request.method == 'POST':
        form = KhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kho')
    else:
        form = KhoForm()
    kho = Kho.objects.all()
    return render(request,'kho.html',{'kho':kho_thuoc},{'form':form})

def lay_thuoc(request):
    thuoc_id = request.GET.get('thuoc_id')
    thuoc = Thuoc.objects.get(id=thuoc_id)
    data = {
        'dvt': thuoc.dvt,
        'don_gia': thuoc.don_gia,
    }
    return JsonResponse(data)