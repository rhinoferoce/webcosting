# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webcosting', '0006_auto_20160517_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degreintegration',
            name='coefficient_integration',
        ),
        migrations.RemoveField(
            model_name='degreintegration',
            name='degre_integration',
        ),
        migrations.RemoveField(
            model_name='degreintegration',
            name='type_attribut',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='degres_integration',
        ),
        migrations.AddField(
            model_name='degreintegration',
            name='projet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webcosting.Projet'),
        ),
    ]
