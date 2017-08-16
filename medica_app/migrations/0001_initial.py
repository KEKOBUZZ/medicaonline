# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adress', models.CharField(blank=True, default='', max_length=150)),
                ('postal_code', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('observaciones', models.CharField(blank=True, default='', max_length=250)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medica_app.Cita')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('gender', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('professional_id', models.CharField(blank=True, default='', max_length=150)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
                ('password', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('gender', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('adress', models.CharField(blank=True, default='', max_length=150)),
                ('postal_code', models.IntegerField(null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
                ('password', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='consultorio',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medica_app.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medica_app.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medica_app.Paciente'),
        ),
    ]
