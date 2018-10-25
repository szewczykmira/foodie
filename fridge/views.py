from rest_framework import generics

from fridge.models import Food
from fridge.serializers import FoodSerializer

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodView(generics.RetrieveDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
