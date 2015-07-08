# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0005_remove_application_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='user',
        ),
    ]
