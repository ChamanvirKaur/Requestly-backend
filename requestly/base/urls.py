from django.urls import path,include
from .views import SimpleView
# from django.contrib.auth.models import Group

urlpatterns = [
    path('',SimpleView, name = 'simple-view')
]
