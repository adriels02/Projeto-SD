# modulo_carrinho/admin.py
from django.contrib import admin
from .models import Compra, DetalhesCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = (
        'id_compra', 'produto_id_externo', 'name', 'price', 'quantidade', 'data_compra', 'email_cliente'
    )
    search_fields = ('name', 'email_cliente')  # Permite buscar por nome e email no painel admin
    list_filter = ('data_compra',)  # Filtros disponíveis na lateral do painel admin
    readonly_fields = ('data_compra',)  # Campos somente leitura

@admin.register(DetalhesCompra)
class DetalhesCompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'email_cliente', 'total_compra')
    search_fields = ('email_cliente',)  # Permite buscar por email no painel admin
    readonly_fields = ('compra',)  # Campos somente leitura
