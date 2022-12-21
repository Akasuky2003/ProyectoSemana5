from users.models import User
from .serializers import SignUpV2Serializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = SignUpV2Serializer
     pagination_class = StandardResultsSetPagination
     filter_backends = [filters.SearchFilter, filters.OrderingFilter]

     search_fields = ['title', 'body']
     ordering = ('-id')