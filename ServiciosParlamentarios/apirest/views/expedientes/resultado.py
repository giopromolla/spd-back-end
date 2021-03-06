from rest_framework import viewsets
from apirest.models.expedientes.resultado import Resultado
from apirest.serializers.expedientes.resultado import ResultadoSerializer
from apirest.filters.expedientes.resultado_filter import ResultadoFilter
from apirest.authorizers.authorizator import has_permission

class ResultadoViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Resultado
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    filter_class = ResultadoFilter
    ordering_fields = '__all__'
    search_fields = ('id', 'resultado','tipo','titulo','sumario','texto')
        
    @has_permission    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los resultados de un expediente.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el resultado solicitado por id de un expediente determinado.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)

    
