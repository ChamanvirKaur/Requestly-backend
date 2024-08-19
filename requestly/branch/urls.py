from django.urls import path, include
from .views import BranchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('branch', BranchViewSet)

urlpatterns = [
    path('', include(router.urls), name='branch'),
]
