from django.shortcuts import render, get_object_or_404
from core.models import Produtos
# Create your views here.

def index(request):

    produto = Produtos.objects.all()
    context = {
        'Chave': 'Valor',
        'produtos': produto
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request,'contact.html')

def produto(request, pd):
    #prod = Produtos.objects.get(id=pd)
    prod = get_object_or_404(Produtos, id=pd)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    return render(request, 'error404.html')