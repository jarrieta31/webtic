# Generated by Django 4.2.1 on 2023-08-21 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaTablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=60, unique=True, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'marca tablet',
                'verbose_name_plural': 'marcas tablets',
                'ordering': ('marca',),
            },
        ),
        migrations.CreateModel(
            name='ModeloTablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=60, unique=True, verbose_name='Modelo')),
            ],
            options={
                'verbose_name': 'modelo tablet',
                'verbose_name_plural': 'modelos tablets',
                'ordering': ('modelo',),
            },
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('equipo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equipos.equipo')),
                ('imei1', models.CharField(max_length=15, unique=True, verbose_name='IMEI 1')),
                ('imei2', models.CharField(max_length=15, unique=True, verbose_name='IMEI 2')),
                ('serie', models.CharField(max_length=15, unique=True, verbose_name='Nro. Serie')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tablets', verbose_name='Imagen')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edidión')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablets.marcatablet', verbose_name='Marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablets.modelotablet', verbose_name='Modelo')),
            ],
            options={
                'verbose_name': 'equipo tablet',
                'verbose_name_plural': 'equipos tables',
                'ordering': ('serie',),
            },
            bases=('equipos.equipo',),
        ),
    ]
