from django.db import models

class Categoria (models.Model): 
    nombre = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto (models.Model): 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=200) 
    precio = models. DecimalField(max_digits=6, decimal_places=2) 
    stock = models.IntegerField(default=0) 
    estado = models.CharField(max_length=100, default='Disponible')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre
    @property
    def estado(self):
        if self.stock > 0:
            return "Disponible"
        else:
            return "Agotado"

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_de_nacimiento = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre

class Inscripcion (models.Model): 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    reserva = models.CharField(max_length=200) 
    precio = models. DecimalField(max_digits=6, decimal_places=2) 
    objeto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.reserva

