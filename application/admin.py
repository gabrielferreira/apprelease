from django.contrib import admin
from .models import Application, Platform, Flavour

class PlatformAdmin (admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        qs = super(PlatformAdmin, self).queryset(request)
        return qs.filter(created_by=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            # the changelist itself
            return True
        return obj.user == request.user

class ApplicationAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        qs = super(ApplicationAdmin, self).queryset(request)
        return qs.filter(created_by=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            # the changelist itself
            return True
        return obj.user == request.user

class FlavourAdmin (admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        qs = super(FlavourAdmin, self).queryset(request)
        return qs.filter(created_by=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            # the changelist itself
            return True
        return obj.user == request.user

admin.site.register(Platform, PlatformAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Flavour, FlavourAdmin)
