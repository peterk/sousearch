# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sousearch', '0002_auto_20150831_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betankande',
            name='txtfile',
            field=models.CharField(max_length=255, verbose_name='Filnamn r\xe5text'),
        ),
    ]
