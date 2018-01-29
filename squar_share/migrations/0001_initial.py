# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DownloadDocount', models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u6b21\u6570')),
                ('code', models.CharField(max_length=8, verbose_name='code')),
                ('Datatime', models.DateTimeField(default=datetime.datetime.now)),
                ('path', models.CharField(max_length=32, verbose_name='\u4e0b\u8f7d\u8def\u5f84')),
                ('name', models.CharField(default=b'', max_length=32, verbose_name='\u6587\u4ef6\u540d')),
                ('Filesize', models.CharField(max_length=10, verbose_name='\u6587\u4ef6\u5927\u5c0f')),
                ('PCIP', models.CharField(default=b'', max_length=32, verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
            ],
            options={
                'db_table': 'download',
                'verbose_name': 'download',
                'verbose_name_plural': 'download',
            },
        ),
    ]
