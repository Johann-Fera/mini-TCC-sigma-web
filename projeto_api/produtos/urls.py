from django.urls import path
from . import views
urlpatterns = [
    path('comidas/', views.ComidaList.as_view(), name='comida-list'),
    path('comidas/<int:pk>/', views.ComidaDetail.as_view(), name='comida-detail'),
]