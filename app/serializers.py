from rest_framework import serializers
from .models import Ds

class Deserilizer(serializers.Serializer):
    name = serializers.CharField(max_length=222)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=222)
    password = serializers.CharField(max_length=222)

    def create(self, validated_data):
        return Ds.objects.create(**validated_data)