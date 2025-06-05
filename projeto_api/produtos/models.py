from django.db import models

class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='comidas/', blank=True, null=True)
    popular = models.BooleanField(default=False)
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    dia = models.DateField()
    hora = models.TimeField()
    pessoas = models.PositiveIntegerField()
    obs = models.TextField()

    def __str__(self):
        return self.nome

class Delivery(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    complemento = models.TextField()
    pagamento = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome