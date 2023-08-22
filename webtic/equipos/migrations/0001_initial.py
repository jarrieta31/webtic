# Generated by Django 4.2.1 on 2023-08-21 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destinos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Nro. Inventario')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.destino', verbose_name='Ubicación')),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
                'ordering': ('item',),
            },
        ),
    ]
