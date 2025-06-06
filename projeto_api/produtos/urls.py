from django.urls import path
from . import views

urlpatterns = [
    path('comidas/', views.ComidaList.as_view(), name='comida-list'),
    path('comidas/<int:pk>/', views.ComidaDetail.as_view(), name='comida-detail'),
    path('reservas/', views.ReservaList.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', views.ReservaDetail.as_view(), name='reserva-detail'),
    path('delivery/', views.DeliveryList.as_view(), name='delivery-list'),
    path('delivery/<int:pk>/', views.DeliveryDetail.as_view(), name='delivery-detail')
]