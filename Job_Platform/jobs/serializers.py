from rest_framework import serializers
from .models import Industry, Location, Company, Job

class IndustrySerializer(serializers.ModelSerializer):
    class Meta: model = Industry; fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta: model = Location; fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta: model = Company; fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
