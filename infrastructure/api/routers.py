from rest_framework.routers import DefaultRouter
from .viewsets import (
    UserViewSet,
    InfrastructureViewSet,
    RoadViewSet,
    BuildingViewSet,
    WardViewSet
)
from utils.offline import OfflineSyncView
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'infrastructure', InfrastructureViewSet, basename='infrastructure')
router.register(r'roads', RoadViewSet, basename='road')
router.register(r'buildings', BuildingViewSet, basename='building')
router.register(r'wards', WardViewSet, basename='ward')

extra_urls = [
    path('offline/sync/', OfflineSyncView.as_view(), name='offline-sync'),
]