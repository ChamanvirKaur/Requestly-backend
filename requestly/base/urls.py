from django.urls import path
from .views import FrontEnd

urlpatterns= [
    path('', FrontEnd, name ="simple_view"),
]