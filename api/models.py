from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 200)

    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)
