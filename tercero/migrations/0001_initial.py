# Generated by Django 5.2.2 on 2025-07-02 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('departamento_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Departamento')),
                ('departamento_codigo', models.CharField(max_length=100, verbose_name='codigo del departamento')),
                ('departamento_nombre', models.CharField(max_length=100, verbose_name='Nombre del departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'DEPARTAMENTOS',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('pais_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID País')),
                ('pais_codigo', models.CharField(max_length=100, verbose_name='codigo del país')),
                ('pais_nombre', models.CharField(max_length=100, verbose_name='Nombre del país')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'PAÍSES',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('municipio_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Municipio')),
                ('municipio_codigo', models.CharField(max_length=100, verbose_name='codigo del municipio')),
                ('municipio_nombre', models.CharField(max_length=100, verbose_name='Nombre del municipio')),
                ('municipio_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='tercero.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'MUNICIPIOS',
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='departamento_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='tercero.pais', verbose_name='País'),
        ),
        migrations.CreateModel(
            name='Terceros',
            fields=[
                ('tercero_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Tercero')),
                ('tercero_codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('tercero_nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('tercero_apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('tercero_razon_social', models.CharField(blank=True, max_length=150, null=True, verbose_name='Razón social')),
                ('tercero_fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('tercero_direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('tercero_telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('tercero_email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('tercero_obligado_facturar', models.BooleanField(default=False, verbose_name='Obligado a facturar')),
                ('tercero_proveedor', models.BooleanField(default=False, verbose_name='Proveedor')),
                ('tercero_tipo', models.CharField(max_length=50, verbose_name='Tipo de tercero')),
                ('tercero_estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('tercero_departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='terceros_departamento', to='tercero.departamento', verbose_name='Departamento')),
                ('tercero_municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='terceros_municipio', to='tercero.municipio', verbose_name='Municipio')),
                ('tercero_pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='terceros_pais', to='tercero.pais', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Tercero',
                'verbose_name_plural': 'TERCEROS',
            },
        ),
    ]
