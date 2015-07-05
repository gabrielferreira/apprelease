# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('release', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Set the flavour name', unique=True, max_length=150, db_index=True)),
                ('slug', models.SlugField(max_length=150)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Set the platform name', unique=True, max_length=50, db_index=True)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(help_text=b'Set the release version', max_length=50, db_index=True)),
                ('release', models.FileField(upload_to=b'releases')),
                ('date', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField()),
                ('flavour', models.ManyToManyField(to='release.Flavour')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('version',),
            },
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='application',
            name='bundle_id',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name=b'Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'logos', blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flavour',
            name='application',
            field=models.ForeignKey(to='release.Application'),
        ),
        migrations.AddField(
            model_name='flavour',
            name='platform',
            field=models.ForeignKey(to='release.Platform'),
        ),
        migrations.AddField(
            model_name='flavour',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='platform',
            field=models.ManyToManyField(to='release.Platform'),
        ),
    ]
