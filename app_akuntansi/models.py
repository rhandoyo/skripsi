from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_profil(models.Model):
    user = models.CharField(User, max_length=100)
    poto = models.ImageField(upload_to='poto', default='', null=True, blank=True)
    status = models.TextField()

    def __str__(self):
        return self.user

class Customer(models.Model):
    nama   = models.CharField(max_length=100)
    email  = models.EmailField(max_length=100, null=True, blank=True)
    alamat = models.CharField(max_length=200)
    telp   = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nama

class Suplier(models.Model):
    nama   = models.CharField(max_length=100)
    email  = models.EmailField(max_length=100)
    alamat = models.CharField(max_length=200)
    telp   = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nama

class Kode_akun(models.Model):
    pilihan_saldo = (
        ('Debit','Debit'),
        ('Kredit','Kredit')
    )
    pilihan_akun_pembayaran = (
        ('Y','Y'),
        ('N','N')
    )

    kode_akun  = models.CharField(max_length=20)
    nama       = models.CharField(max_length=100)
    saldo_normal = models.CharField(max_length=100, choices=pilihan_saldo, blank=True, null=True)
    akun_pembayaran = models.CharField(max_length=100,choices=pilihan_akun_pembayaran, blank=True, null=True)

    def __str__(self):
        return self.kode_akun

class Item_barang(models.Model):
    kode_item  = models.CharField(max_length=50,default='B2IC',blank=False, null=False)
    nama_item  = models.CharField(max_length=100)
    uom        = models.CharField(max_length=100,default='Set')
    harga_beli = models.FloatField(null=True,blank=True)
    harga_jual = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.kode_item

class Pembelian(models.Model):
    nota          = models.CharField(max_length=20,default='')
    tanggal       = models.DateField(auto_now=True, auto_now_add=False)
    pemasok       = models.ForeignKey(Suplier,on_delete=models.CASCADE, default='')
    id_item       = models.CharField(max_length=50,default='B2IC',blank=False, null=False)
    nama          = models.CharField(max_length=100)
    uom           = models.CharField(max_length=50, default='Set')
    harga         = models.FloatField()
    quantity      = models.IntegerField()
    total         = models.FloatField()

    pilihan_status = (
        ('Lunas','Lunas'),
        ('Hutang','Hutang')
    )
    status        = models.CharField(max_length=50,choices= pilihan_status, default='Hutang')
    sudah_dibayar = models.FloatField(blank=True, null=True)
    sisa          = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nama

