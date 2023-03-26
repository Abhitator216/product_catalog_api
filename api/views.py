from django.shortcuts import render
from rest_framework import viewsets,generics, filters
from api.models import Company
from api.serializers import CompanySerializer
from django.http import HttpResponse

class CompanyViewSet(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category', 'brand']
    ordering_fields = ['name', 'category', 'brand']
    
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer   

 


