# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20170405_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]