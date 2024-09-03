from django.shortcuts import render, get_object_or_404
from produtos.models import Product
from django.http import JsonResponse
from django.shortcuts import render
from .models import Compra



def carrinho_view(request):
    # Obtém todos os itens do carrinho
    itens = Compra.objects.all()

    # Calcula o total
    total_preco = sum(item.price * item.quantidade for item in itens)

    return render(request, 'carrinho.html', {
        'itens': itens,
        'total_preco': total_preco,
    })


def adicionar_ao_carrinho(request, produto_id):
    if request.method == 'POST':
        produto = get_object_or_404(Product, id=produto_id)

        # Suponha que o email do cliente seja passado na requisição
        email_cliente = request.POST.get('email_cliente', '')

        compra = Compra(
            produto_id_externo=produto.id,
            name=produto.name,
            price=produto.price,
            image=produto.image,
            quantidade=1,  # Você pode ajustar a quantidade conforme necessário
            email_cliente=email_cliente
        )
        compra.save()

        return JsonResponse({'status': 'success', 'message': 'Produto adicionado ao carrinho'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


def contar_produtos(request):
    count = Compra.objects.count()  # Contar o número de itens no carrinho
    return JsonResponse({'count': count})
