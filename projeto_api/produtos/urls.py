from django.urls import path
from . import views
from .views import criar_pedido

urlpatterns = [
    path('comidas/', views.ComidaList.as_view(), name='comida-list'),
    path('comidas/<int:pk>/', views.ComidaDetail.as_view(), name='comida-detail'),
]

urlpatterns = [
    path('api/pedidos/', criar_pedido, name='criar_pedido'),
]