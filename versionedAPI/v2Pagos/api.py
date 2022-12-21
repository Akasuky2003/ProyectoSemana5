from pagos.models import Pagos
from .serializers import PagoV2Serializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
class PagosViewSet(viewsets.ModelViewSet):
     queryset = Pagos.objects.all()
     serializer_class = PagoV2Serializer
     pagination_class = StandardResultsSetPagination
     filter_backends = [filters.SearchFilter, filters.OrderingFilter]

     search_fields = ['title', 'body']
     ordering = ('-id')