from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.periodo import Periodo

class Publicacion(models.Model):
    id = models.IntegerField(primary_key=True,db_column='publicacion_id')
    fk_periodo = models.ForeignKey(Periodo, db_column='fk_periodo', blank=True, null=True)
    fimpresion = models.DateField(blank=True, null=True)
    tipo = models.TextField(blank=True)
    visibilidad = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().PUBLICACION
        app_label = Constants().APIREST