from rest_framework import serializers
from .models import Application, Platform, Flavour, Release, Environment

# Serializers define the API representation.
class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'slug', 'short_description', 'logo', 'summary', 'platform', 'email', 'bundle_id')

class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Release
        fields = ('version', 'flavour', 'environment', 'date')

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('name', 'slug')

class FlavourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavour
        fields = ('name', 'slug', 'application', 'platform')

class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Environment
        fields = ('name', 'slug', 'application')
