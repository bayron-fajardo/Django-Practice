from django.db import models

class Task(models.Model):
    
    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    state = models.CharField(default="Pendiente", max_length=15)
    fechaInicial = models.DateField()
    fechaEstimada = models.DateField()
    personas = models.ManyToManyField('Person')

class Person(models.Model):

    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    rol = models.CharField(max_length=50)
    yearsExperiencie = models.IntegerField(default=0)
    fechaIngreso = models.DateField()
    tasks = models.ManyToManyField(Task)