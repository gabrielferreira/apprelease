from django.contrib import admin
from .models import Application, Platform, Flavour, Release, Environment

class PlatformAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    list_display = ('name', 'slug')

class ApplicationAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    list_display = ('name', 'slug', 'short_description', 'bundle_id')

class EnvironmentAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    list_display = ('name', 'slug', 'application')

class FlavourAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    list_display = ('name', 'slug', 'application', 'platform')

class ReleaseAdmin (admin.ModelAdmin):
    pass

admin.site.register(Platform, PlatformAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Flavour, FlavourAdmin)
admin.site.register(Release, ReleaseAdmin)
