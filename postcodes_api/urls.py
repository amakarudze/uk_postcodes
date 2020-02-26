from django.urls import re_path

from . import views

urlpatterns = [
    re_path('([\w ]+)/$', views.validate_postcode, name="index"),
]
