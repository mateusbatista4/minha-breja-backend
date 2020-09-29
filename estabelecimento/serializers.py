from rest_framework import serializers

from estabelecimento.models import Estabelecimento
from pedidos.serializers import PedidoSerializer
from produtos.serialazers import ProdutoSerializer


class EstabelecimentoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)
    pedidos = PedidoSerializer(many=True)

    class Meta:
        model = Estabelecimento
        fields = ['id','name','dono_name','cnpj','adress','produtos','pedidos']