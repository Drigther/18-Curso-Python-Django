from django.db import models


class clase(models.Model):

     nombre = models.CharField(blank=False, max_length=100)
     numero_clase = models.IntegerField(blank=True)
     
     def __unicode__(self):
         return "%s" % self.nombre

class Elemento(models.Model):

     nombre = models.CharField(blank=False, max_length=100)
     description = models.TextField(blank=True)
     imagen = models.URLField(blank=True, null=True)
     link = models.URLField(blank=True, null=True)
     mostrar = models.BooleanField(default=True)
     clase = models.ForeignKey(clase)
     
     def __unicode__(self):
         return "%s" % self.nombre