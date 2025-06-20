from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.factura_view import FacturaViewSet
from .views.factura_detalle_view import FacturaDetalleViewSet
from .views.causal_devolucion_view import CausalDevolucionViewSet

router = DefaultRouter()
router.register(r'facturas', FacturaViewSet)
router.register(r'detalles', FacturaDetalleViewSet)
router.register(r'causales', CausalDevolucionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
