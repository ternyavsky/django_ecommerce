from django.shortcuts import render
from main.models import *
from rest_framework.views import APIView
from api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
# Create your views here.





class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


        

    
    