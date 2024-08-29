from django.http import JsonResponse
from .models import Product
import requests

def product_list(request):
    products = Product.objects.all()
    data = list(products.values())  # Converte os produtos em uma lista de dicionários
    return JsonResponse(data, safe=False)