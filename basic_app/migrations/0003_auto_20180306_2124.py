# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20170318_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='location',
        ),
        migrations.RemoveField(
            model_name='school',
            name='name',
        ),
        migrations.RemoveField(
            model_name='school',
            name='principal',
        ),
        migrations.AddField(
            model_name='school',
            name='celular',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='school',
            name='nombre',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='school',
            name='numero_de_apartamento',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='school',
            name='piso',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='school',
            name='torre',
            field=models.CharField(default='', max_length=256),
        ),
    ]
