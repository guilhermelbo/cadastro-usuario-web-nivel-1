from django.db import models

# Create your models here.
from django.db import models

class Endereco(models.Model):
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    pis = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=64)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.nome