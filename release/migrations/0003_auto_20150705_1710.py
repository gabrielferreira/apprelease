# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0002_auto_20150705_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Set the environment name', unique=True, max_length=20, db_index=True)),
                ('slug', models.SlugField(max_length=150)),
                ('application', models.ForeignKey(to='release.Application')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='flavour',
            name='user',
        ),
        migrations.RemoveField(
            model_name='release',
            name='user',
        ),
        migrations.RemoveField(
            model_name='release',
            name='flavour',
        ),
        migrations.AddField(
            model_name='release',
            name='flavour',
            field=models.ForeignKey(default=1, to='release.Environment'),
            preserve_default=False,
        ),
    ]
