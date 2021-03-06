# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text=b'Set the application name', max_length=150, unique=True)),
                ('short_description', models.TextField(help_text=b'Set the short description')),
                ('summary', models.TextField(help_text=b'Set the summary')),
                ('slug', models.SlugField(max_length=150)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'logos')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('bundle_id', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text=b'Set the environment name', max_length=20)),
                ('slug', models.SlugField(max_length=150)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='release.Application')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text=b'Set the flavour name', max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='release.Application')),
            ],
            options={
                'ordering': ('name', 'application', 'platform'),
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text=b'Set the platform name', max_length=50, unique=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(db_index=True, help_text=b'Set the release version', max_length=50)),
                ('release', models.FileField(upload_to=b'releases')),
                ('date', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField()),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='release.Environment')),
                ('flavour', models.ManyToManyField(to='release.Flavour')),
            ],
            options={
                'ordering': ('version',),
            },
        ),
        migrations.AddField(
            model_name='flavour',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='release.Platform'),
        ),
        migrations.AddField(
            model_name='application',
            name='platform',
            field=models.ManyToManyField(to='release.Platform'),
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('version', 'environment')]),
        ),
        migrations.AlterUniqueTogether(
            name='flavour',
            unique_together=set([('name', 'application', 'platform')]),
        ),
        migrations.AlterUniqueTogether(
            name='environment',
            unique_together=set([('name', 'application')]),
        ),
    ]
