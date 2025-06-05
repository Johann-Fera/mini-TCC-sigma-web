from rest_framework import serializers
from .models import Comida
from .models import Pedido

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'  

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'