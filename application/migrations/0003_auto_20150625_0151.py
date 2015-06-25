# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20150625_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(help_text=b'Set the release version', unique=True, max_length=150, db_index=True)),
            ],
            options={
                'ordering': ('version',),
            },
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='flavour',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='platform',
            options={'ordering': ('name',)},
        ),
    ]
