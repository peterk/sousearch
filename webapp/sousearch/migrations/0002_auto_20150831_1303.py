# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sousearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='betankande',
            options={'ordering': ['number'], 'verbose_name': 'Bet\xe4nkande', 'verbose_name_plural': 'Bet\xe4nkanden'},
        ),
        migrations.AddField(
            model_name='betankande',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 13, 3, 32, 598658), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='betankande',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 13, 3, 39, 186806), auto_now=True),
            preserve_default=False,
        ),
    ]
