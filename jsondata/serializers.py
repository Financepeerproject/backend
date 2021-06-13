from rest_framework import serializers
from .models import UploadedData
from django.contrib.auth.models import User
from backend import settings

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedData
        fields = ['userId', 'id', 'title']

class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','is_superuser','first_name', 'last_name']

class UserSerializerWithToken(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
    
        return token
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ['token', 'username', 'password', 'first_name', 'last_name']
    