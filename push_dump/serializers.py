# blog/serializers.py
from rest_framework import serializers
from .models import Push

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Push
        fields = '__all__'