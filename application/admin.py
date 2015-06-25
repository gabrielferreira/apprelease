from django.contrib import admin
from .models import Application
# Register your models here.

class ApplicationAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # readonly_fields = ('slug',)

admin.site.register(Application, ApplicationAdmin)
