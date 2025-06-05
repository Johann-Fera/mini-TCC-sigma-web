from rest_framework import serializers
from .models import Comida, Reserva, Delivery

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'  

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'