# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webcosting', '0002_auto_20160504_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimationcocomo',
            name='projet',
        ),
        migrations.RemoveField(
            model_name='estimationpointdefonction',
            name='language_de_programmation',
        ),
        migrations.RemoveField(
            model_name='estimationpointdefonction',
            name='projet',
        ),
        migrations.RemoveField(
            model_name='estimationpointdefonction',
            name='taille_du_projet',
        ),
        migrations.RemoveField(
            model_name='attribut',
            name='estimation_cocomo',
        ),
        migrations.RemoveField(
            model_name='fonction',
            name='estimation_point_de_fonction',
        ),
        migrations.AddField(
            model_name='attribut',
            name='projet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webcosting.Projet'),
        ),
        migrations.AddField(
            model_name='fonction',
            name='projet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webcosting.Projet'),
        ),
        migrations.AddField(
            model_name='projet',
            name='facteur_ajustement',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='projet',
            name='language_de_programmation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webcosting.LanguageDeProgrammation'),
        ),
        migrations.AddField(
            model_name='projet',
            name='taille_du_projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webcosting.TailleDuProjet'),
        ),
        migrations.AddField(
            model_name='projet',
            name='type_projet',
            field=models.CharField(choices=[('OR', 'organique'), ('SD', 'semi-d\xe9tach\xe9'), ('EM', 'embarqu\xe9')], default='organique', max_length=2),
        ),
        migrations.DeleteModel(
            name='EstimationCocomo',
        ),
        migrations.DeleteModel(
            name='EstimationPointDeFonction',
        ),
    ]
