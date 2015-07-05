from django.contrib import admin
from .models import Application, Platform, Flavour, Release, Environment

class PlatformAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ApplicationAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class EnvironmentAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class FlavourAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ReleaseAdmin (admin.ModelAdmin):
    pass

admin.site.register(Platform, PlatformAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Flavour, FlavourAdmin)
admin.site.register(Release, ReleaseAdmin)
