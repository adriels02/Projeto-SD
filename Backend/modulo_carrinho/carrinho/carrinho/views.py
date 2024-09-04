from django.http import JsonResponse, Http404
from django.db import connection
import requests
from django.shortcuts import redirect

def cart_view(request):
    cart = request.session.get('cart', {})
    itens = []

    
    for product_id, details in cart.items():
        product = get_product_from_service(product_id)
        itens.append({
            'name': product['name'], 
            'price': float(details['price']),  
            'quantity': details['quantity'],
            'image_url': product['image_url'],  
        })

    
    total_preco = sum(item['price'] * item['quantity'] for item in itens)

   
    return JsonResponse({'itens': itens, 'total_preco': total_preco})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_product_from_service(product_id)  

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product['name'],
            'price': str(product['price']),
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('cart_view') 


def get_product_from_service(product_id):
    try:
        
        url = f"http://produtos:8000/products/{product_id}/"
        
     
        response = requests.get(url)
        
       
        if response.status_code == 200:
            
            return response.json()
        else:
            
            raise Http404(f"Product with ID {product_id} not found")
    
    except requests.exceptions.RequestException as e:
        
        raise Http404(f"Error connecting to the product service: {e}")