from rest_framework import viewsets
from apirest.models.relaciones.citacion_gpa_invita_entidad import CitacionGpaInvitaEntidad
from apirest.serializers.individuos.citacion_gpa_invita_entidad import CitacionGpaInvitaEntidadSerializer
from apirest.filters.individuos.invitado_gpa_filter import InvitadoGpaFilter
from apirest.authorizers.authorizator import has_permission

class CitacionGpaInvitaEntidadViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = CitacionGpaInvitaEntidad.objects.all()
    serializer_class = CitacionGpaInvitaEntidadSerializer
    filter_class = InvitadoGpaFilter
    
    @has_permission    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los invitados de Grupos Parlamentarios de Amistad.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un invitado de Grupo Parlamentario de Amistad solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    