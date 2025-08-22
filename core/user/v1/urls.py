from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')), 
]