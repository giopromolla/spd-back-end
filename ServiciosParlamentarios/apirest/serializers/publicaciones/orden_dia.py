from rest_framework import serializers
from apirest.models.publicaciones.orden_dia import OrdenDia

class OrdenDiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrdenDia
#         fields = ('id','fk_despacho','anio','numero','f113')