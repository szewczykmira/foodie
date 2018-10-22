from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from fridge.models import Food
from fridge.serializers import FoodSerializer


class FoodView(GenericAPIView, ListModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)
