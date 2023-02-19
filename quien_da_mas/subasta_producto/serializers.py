from rest_framework import serializers
from .models import Producto
from .models import Usuario
from .models import Subasta
from .models import Pila_subasta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class SubastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subasta
        fields = "__all__"

class Pila_subastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pila_subasta
        fields = "__all__"