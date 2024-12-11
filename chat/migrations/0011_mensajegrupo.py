# Generated by Django 5.0.4 on 2024-11-09 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_alter_cliente_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('leido', models.BooleanField(default=False)),
                ('tipo', models.CharField(choices=[('texto', 'Texto'), ('foto', 'Foto'), ('video', 'Video'), ('archivo', 'Archivo')], max_length=10)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos/')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados_grupo', to='chat.usuario')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='chat.grupochat')),
            ],
        ),
    ]