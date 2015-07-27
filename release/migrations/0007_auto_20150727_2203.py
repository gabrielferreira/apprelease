# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0006_remove_platform_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flavour',
            options={'ordering': ('name', 'application', 'platform')},
        ),
        migrations.AlterField(
            model_name='flavour',
            name='name',
            field=models.CharField(help_text=b'Set the flavour name', max_length=150, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='flavour',
            unique_together=set([('name', 'application', 'platform')]),
        ),
    ]
