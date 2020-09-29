from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from estabelecimento.models import Estabelecimento
from estabelecimento.serializers import EstabelecimentoSerializer


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
