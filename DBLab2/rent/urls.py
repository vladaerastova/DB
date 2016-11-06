from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.rents, name='rents'),
    url(r'^delete_rent', views.delete_rent, name='delete_rent'),
    url(r'^add_rent', views.add_rent, name='add_rent'),
    url(r'^edit_rent', views.edit_rent, name='edit_rent'),
    url(r'^persons', views.persons, name="persons"),
    url(r'^cars', views.cars, name="cars"),
    url(r'^statistics', views.statistics, name="statistics"),
]
