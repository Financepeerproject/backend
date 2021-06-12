from rest_framework import serializers
from .models import UploadedData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedData
        fields = ['userId', 'id', 'title'] 