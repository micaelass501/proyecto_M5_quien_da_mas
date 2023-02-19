from django.contrib import admin
from .models import Usuario
from .models import Producto
from .models import Subasta
from .models import Pila_subasta
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Subasta)
admin.site.register(Pila_subasta)