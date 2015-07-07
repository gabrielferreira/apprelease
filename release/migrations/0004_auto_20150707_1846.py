# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0003_auto_20150705_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='environment',
            field=models.ForeignKey(default=1, to='release.Environment'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='release',
            name='flavour',
        ),
        migrations.AddField(
            model_name='release',
            name='flavour',
            field=models.ManyToManyField(to='release.Flavour'),
        ),
    ]
