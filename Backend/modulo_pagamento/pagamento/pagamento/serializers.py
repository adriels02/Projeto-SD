from rest_framework import serializers
from .models import Produto, Pedido

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'imagem']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'produto', 'quantidade', 'total', 'data']