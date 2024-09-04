from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Produto, Pedido

def produto_detalhes(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'comprar.html', {'produto': produto})

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


