from django.contrib import admin
from .models import (User_profil,Customer,Suplier,
                    Kode_akun,Item_barang,Pembelian
                                            )
# Register your models here.
admin.site.register(User_profil);
admin.site.register(Customer);
admin.site.register(Suplier);
admin.site.register(Kode_akun);
admin.site.register(Item_barang);
admin.site.register(Pembelian);