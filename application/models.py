from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50, help_text='Set the platform name',
                                unique=True, blank=False, null=False, db_index=True)

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
