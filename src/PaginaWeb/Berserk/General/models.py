from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=100, default='',unique = True)
    password = models.CharField(max_length=100, default='')
    cash = models.IntegerField(default=0)
    pais = models.CharField(max_length=100,default='Peru')

    def __str__(self):
        return self.username


class Personaje(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    velocidad_movimiento = models.DecimalField(max_digits=3, decimal_places=2)
    aceleracion = models.DecimalField(max_digits=2, decimal_places=2)
    vida = models.IntegerField(default = '100')
    defensa = models.IntegerField(default = '0')
    damage_ataque_basico = models.IntegerField(default = '5')
    salto = models.DecimalField(max_digits=1, decimal_places=1)
    velocidad_ataque = models.DecimalField(max_digits=2, decimal_places=2)
    estado = models.IntegerField(default='0')
    def __str__(self):
        return self.vida + "\t" + self.defensa

class Mago(models.Model):
    id_personaje = models.OneToOneField(Personaje, on_delete=models.CASCADE)
    energia = models.IntegerField(default='100')
    damage_hechizos = models.IntegerField(default='10')
    def __str__(self):
        return self.energia

class Hechicero(models.Model):
    id_personaje = models.OneToOneField(Personaje, on_delete=models.CASCADE)
    furia = models.IntegerField(default='100')
    def __str__(self):
        return self.furia

class Mascota(models.Model):
    id_personaje = models.OneToOneField(Personaje, on_delete=models.CASCADE)
    damage = models.IntegerField(default=1)
    vida = models.IntegerField(default=0)
    especialidad = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.damage+"\t"+self.vida

class Almacen(models.Model):
    limiteItems = models.IntegerField(default=20)
    def __str__(self):
        return self.limiteItems

class Item(models.Model):
    id_almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    rango = models.IntegerField(default=0)
    peso = models.DecimalField(max_digits=2, decimal_places=2)
    clasificacion = models.IntegerField(default=0)
    costo = models.IntegerField(default=0)
    def __str__(self):
        return self.clasificacion

"""
class Amigos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_amigo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Nickname_amigo = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.Nickname_amigo
"""
