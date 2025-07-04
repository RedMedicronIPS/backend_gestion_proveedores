from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestionProveedores import views
from .views.factura_view import FacturaViewSet
from .views.factura_detalle_view import FacturaDetalleViewSet
from .views.causal_devolucion_view import CausalDevolucionViewSet
from gestionProveedores.views.view import descargar_archivo


router = DefaultRouter()
router.register(r'facturas', FacturaViewSet)
router.register(r'detalles', FacturaDetalleViewSet)
router.register(r'causales', CausalDevolucionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'descargar_archivo/<int:correo_id>/<str:filename>/',
        descargar_archivo,
        name='descargar_archivo'
    ),
]
