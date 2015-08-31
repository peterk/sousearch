# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Betankande',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isbn', models.CharField(help_text=b'Utan bindestreck, t.ex. 9138133938', max_length=20, verbose_name='ISBN-nummer', blank=True)),
                ('number', models.CharField(help_text='T.ex. 1993:21', max_length=20, verbose_name='SOU-nummer')),
                ('title', models.TextField(help_text='\xd6kat personval : bet\xe4nkande', verbose_name='Titel')),
                ('pdf_url', models.URLField(verbose_name='L\xe4nk till PDF-fil', blank=True)),
                ('txtfile', models.CharField(max_length=50, verbose_name='Filnamn r\xe5text')),
                ('libris_uri', models.URLField(help_text='T.ex. http://libris.kb.se/resource/bib/7265056', verbose_name='URI f\xf6r bibpost i Libris', blank=True)),
            ],
        ),
    ]
