from rest_framework.compat import django_filters
from apirest.models.expedientes.resultado import Resultado
from apirest.filters.custom_filter_list import CustomFilterList

class ResultadoFilter(django_filters.FilterSet):
  
    id = CustomFilterList(name="id", lookup_type="in")
    
    class Meta:
        model = Resultado
        fields = ('id',)
