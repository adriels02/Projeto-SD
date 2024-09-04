from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from .models import Produto, Pedido
import requests, json
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404, HttpResponseRedirect

@csrf_exempt
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

@csrf_exempt
def redirect_to_comprar(request, product_id):
    if request.method == 'GET':
        try:
            # Obtém as informações do produto a partir do serviço
            produto_info = get_product_from_service(product_id)
            
            # Adiciona as informações do produto na sessão
            request.session['produto_info'] = produto_info
            
            # Define a URL para a página de compra
            redirect_url = 'http://localhost:9090/comprar.html'
            
            # Retorna a URL de redirecionamento
            return JsonResponse({'redirect_url': redirect_url})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def finalizar_compra_page(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = int(request.POST.get('quantity', 1))
        produto = get_object_or_404(Produto, id=produto_id)

        if quantidade < 1:
            return render(request, 'finalizar_compra.html', {'error': 'Quantidade deve ser pelo menos 1'})

        total = produto.preco * quantidade
        pedido = Pedido.objects.create(
            produto=produto,
            quantidade=quantidade,
            total=total,
            usuario=request.user
        )

        return render(request, 'finalizar_compra.html', {'pedido': pedido})
    
    return render(request, 'finalizar_compra.html')

def comprar_view(request):
    
    produto_info = request.session.get('produto_info', {})

    if not produto_info:
        return JsonResponse({'error': 'Informações do produto não encontradas na sessão'}, status=404)

    return JsonResponse({
        'name': produto_info.get('name'),
        'price': produto_info.get('price'),
        'description': produto_info.get('description'),
        'image_url': produto_info.get('image_url'),
    })