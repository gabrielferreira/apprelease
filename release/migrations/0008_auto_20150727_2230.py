# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0007_auto_20150727_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='name',
            field=models.CharField(help_text=b'Set the environment name', max_length=20, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='environment',
            unique_together=set([('name', 'application')]),
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('version', 'environment')]),
        ),
    ]
