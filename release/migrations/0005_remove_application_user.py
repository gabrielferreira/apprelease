# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0004_auto_20150707_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
    ]
