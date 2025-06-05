from django.shortcuts import render
from rest_framework import generics
from .models import Comida
from .serializers import ComidaSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PedidoSerializer


class ComidaList(generics.ListCreateAPIView):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer
class ComidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer


@api_view(['POST'])
def criar_pedido(request):
    serializer = PedidoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "Pedido criado com sucesso"})
    return Response(serializer.errors, status=400)