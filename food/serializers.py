from rest_framework import serializers
from . models import myfood

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = myfood
        fields=['beverage']

