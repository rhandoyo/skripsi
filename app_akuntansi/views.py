from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Sum
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth import authenticate, login, logout
from .models import (User_profil,Customer,Suplier,
                     Kode_akun,Item_barang,Pembelian,
                                                      )
# Create your views here.


class Dashboard(TemplateView):
    template_name = 'dashboard.html'

def customer(requset):
    customers = Customer.objects.all();
    context = {
        'head':'Customer',
        'customer':customers
    }
    return render(requset,'customer.html',context)

def edit_customer(request,id_input):
    cust_edit = Customer.objects.get(id=id_input)
    context = {
        'head':'Update Customer',
        'cust_edit':cust_edit
    }
    if request.method == 'POST':
        cust_edit = Customer.objects.get(id=id_input)
    
        cust_edit.nama   = request.POST.get('nama')
        cust_edit.email  = request.POST.get('email')
        cust_edit.alamat = request.POST.get('alamat')
        cust_edit.telp   = request.POST.get('telepon')

        cust_edit.save(); 

        return redirect('app_akuntansi:customer')
    return render(request,'edit_customer.html',context)

def tambah_customer(request):
    context = {
        'head':'Form Tambah Customer'
    }
    
    if request.method == 'POST':
        Customer.objects.create(
            nama   = request.POST.get('nama'),  
            email  = request.POST.get('email'),
            alamat = request.POST.get('alamat'),
            telp   = request.POST.get('telepon')
        )
        Customer.save
        return redirect('app_akuntansi:customer')
    return render(request,'tambah_customer.html',context)

def customer_delete(request, id_input):
    Customer.objects.get(id=id_input).delete();

    return redirect('app_akuntansi:customer')

def suplier(request):
    supliers = Suplier.objects.all();
    context= {
        'head':'Data Suplier',
        'suplier':supliers
    }
    return render(request,'suplier.html',context)

def tambah_suplier(request):
    context = {
        'head':'Form Tambah Suplier'
    }
    
    if request.method == 'POST':
        Suplier.objects.create(
            nama   = request.POST.get('nama'),  
            email  = request.POST.get('email'),
            alamat = request.POST.get('alamat'),
            telp   = request.POST.get('telepon')
        )
        Suplier.save
        return redirect('app_akuntansi:suplier')
    return render(request,'tambah_suplier.html',context)
    
def suplier_delete(request,id_input):
    Suplier.objects.get(id=id_input).delete()

    return redirect('/suplier')
    
def edit_suplier(request,id_input):
    supl_edit = Suplier.objects.get(id=id_input)
    context = {
        'head':'Update Suplier',
        'supl_edit':supl_edit
    }
    if request.method == 'POST':
        supl_edit = Suplier.objects.get(id=id_input)
    
        supl_edit.nama   = request.POST.get('nama')
        supl_edit.email  = request.POST.get('email')
        supl_edit.alamat = request.POST.get('alamat')
        supl_edit.telp   = request.POST.get('telepon')

        supl_edit.save(); 

        return redirect('app_akuntansi:suplier')
    return render(request,'edit_suplier.html',context)

# form kode akun
def kode_akun(request):
    kode_akuns = Kode_akun.objects.all()
    context = {
        'head':'Kode akun',
        'kode_akun':kode_akuns
    }
    return render(request,'kode_akun.html',context)

def tambah_kode_akun(request):
    context = {
        'head':'Form Tambah Kode Akun'
    }
    if request.method == 'POST':
        Kode_akun.objects.create(

        kode_akun = request.POST.get('kode_akun'),
        nama      = request.POST.get('nama'),
        saldo_normal = request.POST.get('saldo_normal'),
        akun_pembayaran = request.POST.get('akun_pembayaran')
        )
        Kode_akun.save

        return redirect('app_akuntansi:kode_akun')
    return render(request,'tambah_akun.html',context)

def kode_akun_delete(request,id_input):
    kode_akun_del = Kode_akun.objects.get(id=id_input).delete()
    
    return redirect('app_akuntansi:kode_akun')

def edit_kode_akun(request,id_input):
    akun_edit = Kode_akun.objects.get(id=id_input);
    context = {
        'head':'Edit Kode Akun',
        'akun_edit':akun_edit
    }
    if request.method == 'POST':
        akun_edit.kode_akun = request.POST.get('kode_akun')
        akun_edit.nama = request.POST.get('nama')
        akun_edit.saldo_normal = request.POST.get('saldo_normal')
        akun_edit.akun_pembayaran = request.POST.get('akun_pembayaran')
        akun_edit.save()

        return redirect('app_akuntansi:kode_akun')
    return render(request,'edit_kode_akun.html',context)

def item(request):
    semua_item = Item_barang.objects.all()
    context = {
        'head':'Item Barang',
        'item':semua_item
    }

    return render(request,'item.html',context)

def tambah_item(request):
    context = {
        'head':'Tambah Item'
    }

    if request.method == 'POST':
        Item_barang.objects.create(
            kode_item  = request.POST.get('kode_item'),
            nama_item  = request.POST.get('nama_item'),
            uom        = request.POST.get('uom'),
            harga_beli = float(request.POST.get('harga_beli')),
            harga_jual = float(request.POST.get('harga_jual')),
        )

        Item_barang.save

        return redirect('app_akuntansi:item')
    return render(request,'tambah_item.html',context)

def item_hapus(request,id_input):
    Item_barang.objects.get(id=id_input).delete()

    return redirect('app_akuntansi:item')

def edit_item(request, id_input):
    item_edit = Item_barang.objects.get(id=id_input);
    context = {
        'head':'Edit Item',
        'item_edit':item_edit
    }
    if request.method == 'POST':
        item_edit.kode_item = request.POST.get('kode_item')
        item_edit.nama_item = request.POST.get('nama_item')
        item_edit.uom  = request.POST.get('uom')
        item_edit.harga_beli = request.POST.get('harga_beli')
        item_edit.harga_jual = request.POST.get('harga_jual')

        item_edit.save();

        return redirect('app_akuntansi:item')

    return render(request,'edit_item.html',context)

def pembelian(request):
    pembelians = Pembelian.objects.all();
    for p in pembelians:
        tahun = p.tanggal
        print(tahun)
    context = {
        'head':'Data Pembelian',
        'pembelians':pembelians
    }
    return render(request,'purchase_order.html',context)

def form_transaksi_pembelian(request):
    item_barangs = Item_barang.objects.all();
    supliers = Suplier.objects.all();
    pembelians = Pembelian.objects.all();

    grand_total = Pembelian.objects.aggregate(Sum('total'))

    print(grand_total);

    context = {
        'head':'Form Transaksi Pembelian',
        'items':item_barangs,
        'supliers':supliers,
        'pembelians':pembelians,
        'total': grand_total['total__sum']
    }

    if request.method == 'POST':
        harga      = int(request.POST.get('harga'))
        quantity   = int(request.POST.get('quantity'))

        total_harga = int(harga*quantity)

        Pembelian.objects.create(
            nota       = request.POST.get('nota_number'),
            tanggal    = request.POST.get('tanggal'),
            pemasok_id = request.POST.get('pemasok'),
            id_item    = request.POST.get('id_item'),
            nama       = request.POST.get('item_nama'),
            uom        = request.POST.get('uom'),
            harga      = request.POST.get('harga'),
            quantity   = request.POST.get('quantity'),
            total      = total_harga
            
        )
        Pembelian.save

        return redirect('/transaksiPembelian/')

    return render(request,'form_transaksi_pembelian.html',context)

def edit_form_pembelian(request, id):
    form_edit = Pembelian.objects.get(id=id);
    supliers = Suplier.objects.all();
    item_barangs = Item_barang.objects.all();
    context = {
        'form_edit':form_edit,
        'supliers':supliers,
        'items':item_barangs
    }

    if request.method == 'POST':
        harga      = float(request.POST.get('harga'))
        quantity   = float(request.POST.get('quantity'))

        total_harga = float(harga*quantity)
        
        form_edit.nota       = request.POST.get('nota_number')
        form_edit.tanggal    = request.POST.get('tanggal')
        form_edit.pemasok_id = request.POST.get('pemasok')
        form_edit.id_item    = request.POST.get('id_item')
        form_edit.nama       = request.POST.get('item_nama')
        form_edit.uom        = request.POST.get('uom')
        form_edit.quantity   = request.POST.get('quantity')
        form_edit.total      = total_harga
        
        form_edit.save();

        return redirect('app_akuntansi:form_transaksi_pembelian')
    return render(request,'edit_form_pembelian.html',context)

def hapus_form_pembelian(request, id):
    Pembelian.objects.filter(id=id).delete()
    return redirect('app_akuntansi:form_transaksi_pembelian')


def penjualan(request):
    context = {
        'head':'Form penjualan'
    }
    return render(request,'form_penjualan', context)








    

