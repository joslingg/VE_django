from django.shortcuts import render,get_object_or_404,redirect
from .models import Thuoc
from .forms import DanhMucForm

def danh_muc_thuoc(request):
    thuoc = Thuoc.objects.all()
    return render(request, 'danh_muc.html', {'thuoc': thuoc})

def them_danh_muc(request):
    if request.method == 'POST':
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_muc_thuoc')
    else:
        form = DanhMucForm()
    thuoc = Thuoc.objects.all()
    return render(request,'danh_muc.html',{'danh_muc_thuoc':danh_muc_thuoc},{'form':form})

def sua_danh_muc(request):
    thuoc = get_object_or_404(Thuoc, id=id)
    if request.method == 'POST':
        form = DanhMucForm(request.POST, instance=thuoc)
        if form.is_valid():
            form.save()
            return redirect('danh_muc_thuoc')
    else:
        form =  DanhMucForm(instance=thuoc)
    thuoc = Thuoc.objects.all()
    return render(request,'danh_muc.html',{'danh_muc_thuoc':danh_muc_thuoc},{'form':form})