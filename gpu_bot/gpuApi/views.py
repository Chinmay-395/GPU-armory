from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/item-list/',
        'Detail View': '/item-detail/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def itemList(request):
    item = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def itemDetail(request, pk):
    item = Product.objects.get(id=pk)
    serializer = ProductSerializer(item, many=False)
    return Response(serializer.data)
