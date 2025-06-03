from django.shortcuts import render
from rest_framework import generics
from .models import Comida
from .serializers import ComidaSerializer

class ComidaList(generics.ListCreateAPIView):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer
class ComidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer
