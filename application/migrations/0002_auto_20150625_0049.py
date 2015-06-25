# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Set the flavour name', unique=True, max_length=150, db_index=True)),
                ('slug', models.SlugField(max_length=150)),
                ('application', models.ForeignKey(to='application.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Set the platform name', unique=True, max_length=50, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='flavour',
            name='platform',
            field=models.ForeignKey(to='application.Platform'),
        ),
        migrations.AddField(
            model_name='application',
            name='platform',
            field=models.ManyToManyField(to='application.Platform'),
        ),
    ]
