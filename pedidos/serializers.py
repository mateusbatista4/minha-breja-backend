from  rest_framework import serializers

from produtos.serialazers import ProdutoSerializer
from .models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id','date','produtos','obs','estabelecimento']