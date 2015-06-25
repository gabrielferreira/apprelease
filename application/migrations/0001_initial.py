# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Set the application name', unique=True, max_length=150, db_index=True)),
                ('short_description', models.TextField(help_text=b'Set the short description')),
                ('summary', models.TextField(help_text=b'Set the summary')),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
    ]
