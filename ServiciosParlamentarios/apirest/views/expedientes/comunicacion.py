from rest_framework import viewsets, filters
from apirest.models.expedientes.comunicacion import Comunicacion
from apirest.serializers.expedientes.comunicacion import ComunicacionSerializer
from apirest.filters.expedientes.comunicacion_filter import ComunicacionFilter
from apirest.authorizers.authorizator import has_permission

class ComunicacionViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Comunicacion
    queryset = Comunicacion.objects.all()
    serializer_class = ComunicacionSerializer
    filter_class = ComunicacionFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todas las comunicaciones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una comunicacion solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)