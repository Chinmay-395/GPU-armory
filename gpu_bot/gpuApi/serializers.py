from rest_framework import serializers
from gpuApi.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'Architecture')
