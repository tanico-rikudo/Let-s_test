from django.conf.urls import url
from testor import views

urlpatterns = [
    url(r'^members$', views.index, name='index'),#in app
]