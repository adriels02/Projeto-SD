from rest_framework import serializers
from .models import Compra, DetalhesCompra

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = [
            'id_compra', 'produto_id_externo', 'name', 'price', 'image',
            'quantidade', 'data_compra', 'email_cliente'
        ]

class DetalhesCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalhesCompra
        fields = ['compra', 'email_cliente', 'total_compra'
                  ]
