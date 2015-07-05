from rest_framework import serializers
from .models import Application

# Serializers define the API representation.
class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'slug', 'short_description', 'logo')
