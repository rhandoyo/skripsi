# Generated by Django 2.0 on 2020-08-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_akuntansi', '0005_remove_pembelian_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembelian',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
