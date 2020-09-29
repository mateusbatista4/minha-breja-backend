from django.db import models

# Create your models here.
from produtos.models import Produto


class Estabelecimento(models.Model):
    name = models.CharField(max_length=100)
    dono_name = models.CharField(max_length=100,null=True,blank=True)
    cnpj = models.CharField(max_length=20)
    adress = models.CharField(max_length=150)
    produtos = models.ManyToManyField(Produto,blank=True,null=True)

    def __str__(self):
        return self.name