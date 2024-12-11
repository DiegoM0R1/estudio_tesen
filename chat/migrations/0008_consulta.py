# Generated by Django 5.0.4 on 2024-11-07 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_oportunidad_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('resuelto', 'Resuelto')], default='pendiente', max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_resolucion', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='chat.cliente')),
            ],
        ),
    ]