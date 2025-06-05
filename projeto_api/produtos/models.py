from django.db import models

class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='comidas/', blank=True, null=True)
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=50)
    itens = models.TextField()  

    def __str__(self):
        return self.nome