from django.conf.urls import url

from fridge import views

urlpatterns = [
    url(r"^$", views.FoodList.as_view(), name="home"),
]
