from django.shortcuts import render
from rest_framework import generics
from .models import Comida, Reserva, Delivery
from .serializers import ComidaSerializer, ReservaSerializer, DeliverySerializer

class ComidaList(generics.ListCreateAPIView):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer
class ComidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer