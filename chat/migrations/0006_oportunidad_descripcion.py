# Generated by Django 5.0.4 on 2024-11-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_cobranza_factura_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='descripcion',
            field=models.TextField(default='Sin descripción'),
            preserve_default=False,
        ),
    ]