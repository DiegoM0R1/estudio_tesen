# Generated by Django 5.0.4 on 2024-11-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_cobranza_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='origen',
            field=models.CharField(choices=[('venta', 'Venta'), ('cobranza', 'Cobranza'), ('otro', 'Otro')], default='otro', max_length=50),
            preserve_default=False,
        ),
    ]