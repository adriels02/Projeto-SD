from django.http import JsonResponse, Http404
from .models import Product
import requests

def product_list(request):
    products = Product.objects.all()
    data = list(products.values())  # Converte os produtos em uma lista de dicionários
    return JsonResponse(data, safe=False)

def product_detail(request, product_id):
    try:
       
        product = Product.objects.get(id=product_id)
        
        
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price), 
            'image_url': product.image.url if product.image else None,
        }
        
        
        return JsonResponse(product_data)
    
    except Product.DoesNotExist:
        
        raise Http404(f"Product with ID {product_id} not found")