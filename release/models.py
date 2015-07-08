from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50, help_text='Set the platform name',
                                unique=True, blank=False, null=False, db_index=True)
    user = models.ForeignKey(User)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Application(models.Model):
    name = models.CharField(max_length=150, help_text='Set the application name',
                                unique=True, blank=False, null=False, db_index=True)
    short_description = models.TextField(help_text='Set the short description',
                                blank=False, null=False)
    summary = models.TextField(help_text='Set the summary', blank=False,
                                null=False)
    slug = models.SlugField(max_length=150)
    platform = models.ManyToManyField('Platform')
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    email = models.EmailField('Email', null=False, blank=False)
    bundle_id = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Environment(models.Model):
    name = models.CharField(max_length=20, help_text='Set the environment name',
                                unique=True, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=150)
    application = models.ForeignKey('Application')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Flavour(models.Model):
    name = models.CharField(max_length=150, help_text='Set the flavour name',
                                unique=True, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=150)
    application = models.ForeignKey('Application')
    platform = models.ForeignKey('Platform')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Release(models.Model):
    version = models.CharField(max_length=50, help_text='Set the release version',
                                blank=False, null=False, db_index=True)
    flavour = models.ManyToManyField('Flavour')
    environment = models.ForeignKey('Environment')
    release = models.FileField(upload_to='releases', null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    notes = models.TextField()

    def __unicode__(self):
        return self.version

    class Meta:
        ordering = ('version',)
