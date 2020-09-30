from django.urls import path
from .import views

app_name = 'app_akuntansi'

urlpatterns = [
    path('',views.Dashboard.as_view(), name='dashboard'),
    path('customer/',views.customer, name='customer'),
    path('customer/edit/<int:id_input>/', views.edit_customer, name='edit_customer'),
    path('customer/delete/<int:id_input>/',views.customer_delete, name='customer_delete'),
    path('addcustomer/',views.tambah_customer, name='tambah_customer'),
    path('suplier/',views.suplier, name='suplier'),
    path('addsuplier/',views.tambah_suplier,name='tambah_suplier'),
    path('suplier/delete/<int:id_input>/',views.suplier_delete, name='suplier_delete'),
    path('suplier/edit/<int:id_input>/', views.edit_suplier, name='edit_suplier'),
    path('kode_akun/', views.kode_akun, name='kode_akun'),
    path('addkode_akun/', views.tambah_kode_akun, name='tambah_kode_akun'), 
    path('kode_akun/delete/<int:id_input>/',views.kode_akun_delete, name='kode_akun_delete'),
    path('edit_kode_akun/<int:id_input>/',views.edit_kode_akun, name='edit_kode_akun'),
    path('item/',views.item, name='item'),
    path('addItem/',views.tambah_item,name='tambah_item'),
    path('item/delete/<int:id_input>/',views.item_hapus,name='item_hapus'),
    path('edit_item/<int:id_input>/',views.edit_item,name='edit_item'),
    path('pembelian/',views.pembelian, name='pembelian'),
    path('transaksiPembelian/',views.form_transaksi_pembelian, name='form_transaksi_pembelian'),
    path('editDataPembelian/<int:id>/',views.edit_form_pembelian, name='edit_data_pembelian'),
    path('pembelian/delete/<int:id>/', views.hapus_form_pembelian, name='hapus_pembelian'),
    path('penjualan/', views.penjualan, name='penjualan'),
]   
