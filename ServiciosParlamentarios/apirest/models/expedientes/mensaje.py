from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class Mensaje(models.Model):
    id = models.IntegerField(primary_key=True,db_column='mensaje_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    num = models.CharField(max_length=10)
    anio = models.CharField(max_length=4)
    fecha = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = Constants().MENSAJE
        app_label = Constants().APIREST