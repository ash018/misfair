from .models import *
from rest_framework import serializers

class RegisteredStgSerializer(serializers.ModelSerializer):
    json = serializers.SerializerMethodField('clean_json')
    class Meta:
        model = District
        fields = ('Id', 'DistrictName')