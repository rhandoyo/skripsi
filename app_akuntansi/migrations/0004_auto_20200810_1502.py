# Generated by Django 2.0 on 2020-08-10 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_akuntansi', '0003_auto_20200810_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembelian',
            name='sisa',
        ),
        migrations.RemoveField(
            model_name='pembelian',
            name='sudah_dibayar',
        ),
    ]
