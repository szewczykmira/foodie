from django.conf.urls import url

from fridge import views

urlpatterns = [
    url(r"^$", views.FoodView.as_view(), name="home"),
]
