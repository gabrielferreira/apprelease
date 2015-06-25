from django.contrib import admin
from .models import Application, Platform, Flavour

class PlatformAdmin (admin.ModelAdmin):
    pass

class ApplicationAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # readonly_fields = ('slug',)

class FlavourAdmin (admin.ModelAdmin):
    pass

admin.site.register(Platform, PlatformAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Flavour, FlavourAdmin) 
