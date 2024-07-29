from django.shortcuts import render, redirect
from django.http import HttpResponse
from qlnv.models import *
import json
def index(request):
    data = NhanVien.objects.all()
    return render(request, 'result.html', {'employees': data})

def getNhanVienInfo(request, id):
    data1 = NhanVien.objects.get(id=id)
    data2 = NhanVien.objects.all()
    return render(request, 'result.html', {"employee": data1, 'employees': data2})

def create(request):
    data = request.POST
    print(data)
    nhanvien =NhanVien( ma_nhan_vien = data.get('ma_nhan_vien'), 
                     ho_ten_nhan_vien=data.get('ho_ten_nhan_vien'),
                     luong_co_ban = data.get('luong_co_ban'),
                     loai_nhan_vien = data.get('loai_nhan_vien'),
                     luong_hang_thang = data.get('luong_hang_thang'))
    nhanvien.save()
    data = NhanVien.objects.all()
    return render(request, 'result.html', {"employees": data})

def salaryCalculation(request):
    nhanvien = NhanVien.objects.all()
    list(map(lambda x: x.tinhluong(), nhanvien))

    return redirect('/')

def update(request, id):
    data = request.POST

    nhanvien = NhanVien.objects.get(ma_nhan_vien=id)
    nhanvien.ma_nhan_vien = data.get('ma_nhan_vien')
    nhanvien.ho_ten_nhan_vien = data.get('ho_ten_nhan_vien')
    nhanvien.luong_co_ban = data.get('luong_co_ban')
    nhanvien.loai_nhan_vien = data.get('loai_nhan_vien')
    
    nhanvien.save()

    return redirect('/')

def delete(request, id):
    nhanvien = NhanVien.objects.get(id=id)
    nhanvien.delete()
    return redirect('/')