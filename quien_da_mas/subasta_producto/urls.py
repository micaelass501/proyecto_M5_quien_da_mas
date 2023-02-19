from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"productos",views.ProductoViewSet)
router.register(r"usuarios",views.UsuarioViewSet)
router.register(r"subastas",views.SubastaViewSet)
router.register(r"pila_subastas",views.Pila_subastaViewSet)

urlpatterns = [
    # path("", views.index, name = "index")
    path('contact/<str:name>',views.contact, name='contacto'),
    path('', include(router.urls)),
    path('productosRegistrados/cantidad/',views.producto_count, name="contador"),
]
