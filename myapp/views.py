from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializer import ProductSerializer
# Create your views here.


class ProductApi(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer