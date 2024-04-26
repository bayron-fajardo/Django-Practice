from django.db import models


class Usuario(models.Model):

    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=15)
    correo = models.CharField(max_length=60, default="")
    contrasena =  models.CharField(max_length=15)

    def __str__(self):
        return f'Codigo: {self.id}, Nombre: {self.nombre}, Usuario: {self.usuario}'