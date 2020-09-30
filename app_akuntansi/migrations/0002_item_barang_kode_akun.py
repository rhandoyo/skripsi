# Generated by Django 2.0 on 2020-08-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_akuntansi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_item', models.CharField(default='B2IC', max_length=50)),
                ('nama_item', models.CharField(max_length=100)),
                ('uom', models.CharField(default='Set', max_length=100)),
                ('harga_beli', models.FloatField(blank=True, null=True)),
                ('harga_jual', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kode_akun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_akun', models.CharField(max_length=20)),
                ('nama', models.CharField(max_length=100)),
                ('saldo_normal', models.CharField(blank=True, choices=[('Debit', 'Debit'), ('Kredit', 'Kredit')], max_length=100, null=True)),
                ('akun_pembayaran', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], max_length=100, null=True)),
            ],
        ),
    ]
