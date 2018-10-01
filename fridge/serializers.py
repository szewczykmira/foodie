from rest_framework import serializers

from .models import Food

class FoodSerializer(serializers.Serializer):
    class Meta:
        model = Food
        fields = ('since_when', 'expiration_date', 'name', 'quantity')