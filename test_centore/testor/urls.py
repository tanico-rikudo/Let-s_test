from django.conf.urls import url
from testor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#in app
    url(r'^members$', views.member_index, name='index'),#in app
    url(r'^tests$', views.test_index, name='index'),#in app
    url(r'^middle$', views.middle_index, name='index'),
]