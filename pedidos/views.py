from django.shortcuts import render
from rest_framework import viewsets
from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

   # def list(self, request, *args, **kwargs):
    #    queryset = Pedido.objects.all()
     #   serializer = PedidoMiniSerializer(queryset, many=True)
      #  return Response(serializer.data)