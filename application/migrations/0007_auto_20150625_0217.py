# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0006_auto_20150625_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='bundle_id',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default='admin@admin.com', max_length=254, verbose_name=b'Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'logos', blank=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='slug',
            field=models.SlugField(default=str(uuid.uuid1())),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now(), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='flavour',
            field=models.ManyToManyField(to='application.Flavour'),
        ),
        migrations.AddField(
            model_name='release',
            name='notes',
            field=models.TextField(default='note'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='release',
            field=models.FileField(default=str(uuid.uuid1()), upload_to=b'releases'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
