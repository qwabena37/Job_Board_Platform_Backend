from rest_framework import serializers
from .models import ApplyJob

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = "__all__"
        read_only_fields = ("applicant", "created_at")
