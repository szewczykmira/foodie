from rest_framework import generics

from fridge.models import Food
from fridge.serializers import FoodSerializer

class FoodList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
