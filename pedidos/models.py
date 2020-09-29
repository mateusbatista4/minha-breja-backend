from django.db import models
from produtos.models import Produto
from estabelecimento.models import  Estabelecimento
from django.conf import settings

# Create your models here.
class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto,blank=True,null=True)
    obs = models.CharField(max_length=250)
    date = models.DateTimeField()
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE,related_name="pedidos"),
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE,related_name="pedidos")

    def __str__(self):
        return "Pedido "+ str(self.id)