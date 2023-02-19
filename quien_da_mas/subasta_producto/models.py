from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    ci = models.IntegerField(default=0)
    base_monetaria = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    cantidad = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.nombre} = >{self.descripcion}"
    
class TipoMoneda(models.TextChoices):
    dolar = '$', 'dolares',
    boliviano = 'Bs', 'bolivianos',
    
class Subasta(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_base = models.IntegerField(default=0)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    disponible = models.BooleanField(blank=True, default=True)
    moneda = models.CharField(
        max_length=50,
        choices=TipoMoneda.choices,
        default=TipoMoneda.boliviano
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Producto} = >{self.precio_base}"

class Pila_subasta(models.Model):
    oferta =  models.IntegerField()
    fecha = models.DateTimeField()
    orden = models.IntegerField()
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.Usuario} eligio = >{self.Subasta} : ofertó => {self.oferta}"
