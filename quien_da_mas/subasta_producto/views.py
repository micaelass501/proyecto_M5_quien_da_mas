from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Producto
from .models import Usuario
from .models import Subasta
from .models import Pila_subasta
from .serializers import ProductoSerializer, UsuarioSerializer, SubastaSerializer, Pila_subastaSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class SubastaViewSet(viewsets.ModelViewSet):
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    
class Pila_subastaViewSet(viewsets.ModelViewSet):
    queryset = Pila_subasta.objects.all()
    serializer_class = Pila_subastaSerializer
    
@api_view(["GET"])
def producto_count(request):
    """
    Cantidad de items, ACCES ROL:_ANONYMOUS
    Cantidad de items registrados
    """
    try:
        cantidad =  Producto.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)  
         

