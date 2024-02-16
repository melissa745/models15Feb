# Generated by Django 5.0.1 on 2024-02-14 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaInteligente', '0002_alter_usuario_cedula_alter_usuario_numero_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_proceso', models.IntegerField(unique=True)),
                ('nombre_procesado', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='archivo',
            name='texto_extraido',
        ),
        migrations.RemoveField(
            model_name='archivo',
            name='tipo',
        ),
        migrations.CreateModel(
            name='AdministrativoLaboral',
            fields=[
                ('caso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaInteligente.caso')),
                ('ley_laboral', models.CharField(help_text='Ley o regulación laboral que es relevante para el caso administrativo o laboral.', max_length=255)),
            ],
            bases=('SistemaInteligente.caso',),
        ),
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('caso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaInteligente.caso')),
                ('monto_disputa', models.DecimalField(decimal_places=2, help_text='Monto económico en disputa en el caso civil.', max_digits=10)),
            ],
            bases=('SistemaInteligente.caso',),
        ),
        migrations.CreateModel(
            name='Constitucional',
            fields=[
                ('caso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaInteligente.caso')),
                ('articulo_constitucional', models.CharField(help_text='Artículo de la constitución que es relevante para el caso.', max_length=255)),
            ],
            bases=('SistemaInteligente.caso',),
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('caso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaInteligente.caso')),
                ('relacion_partes', models.CharField(help_text='Relación entre las partes involucradas en el caso de familia.', max_length=255)),
            ],
            bases=('SistemaInteligente.caso',),
        ),
        migrations.CreateModel(
            name='Penal',
            fields=[
                ('caso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaInteligente.caso')),
                ('delito', models.CharField(help_text='Tipo de delito asociado con el caso penal.', max_length=255)),
            ],
            bases=('SistemaInteligente.caso',),
        ),
        migrations.CreateModel(
            name='Sancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sancion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_imposicion', models.DateField()),
                ('fecha_cumplimiento', models.DateField(blank=True, null=True)),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaInteligente.caso')),
            ],
        ),
    ]