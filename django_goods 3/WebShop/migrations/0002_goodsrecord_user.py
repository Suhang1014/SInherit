# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-02 21:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebShop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_record', to=settings.AUTH_USER_MODEL),
        ),
    ]
