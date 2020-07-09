from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet, mixins
from gpuApi.serializers import ProductSerializer
from gpuApi.models import Product
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


# this works
''' this allows the user to put,
    patch, create and delete 
    gpu-items which we dont need
    therefore will try mixins
'''


class GpuViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    search_fields = ['name', ]
    http_method_names = ['get', ]
