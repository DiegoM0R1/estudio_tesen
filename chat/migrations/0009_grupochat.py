# Generated by Django 5.0.4 on 2024-11-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('miembros', models.ManyToManyField(to='chat.usuario')),
            ],
        ),
    ]
