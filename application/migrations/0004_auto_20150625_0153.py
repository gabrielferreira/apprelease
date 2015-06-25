# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20150625_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='version',
            field=models.CharField(help_text=b'Set the release version', max_length=50, db_index=True),
        ),
    ]
