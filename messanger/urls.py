from django.conf.urls import url

from messanger import views

urlpatterns = [
    url(r'^$', views.message, name="messanger"),
]
