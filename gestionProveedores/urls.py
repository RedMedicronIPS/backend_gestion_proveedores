from rest_framework.routers import DefaultRouter
from .views import FacturaViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'factura', FacturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


