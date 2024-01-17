from guestpreferenceapp.models import *
from rest_framework import serializers


class Preferenceserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Preferencemodel
        fields = '__all__'