from rest_framework.routers import DefaultRouter
from .views import TerceroViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'terceros', TerceroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
