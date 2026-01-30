from django.shortcuts import render
from .models import *
# Create your views here.

def homepage(request):
    banners = Banner.objects.filter(ativo=True) #filter em Banner.ativo = True (só pega os banners ativos)
    context = {"banners": banners}
    return render(request,"homepage.html", context) #paginas do site

def loja(request, nome_categoria=None):
    print(nome_categoria)
    produtos = Produto.objects.filter(ativo=True) #aqui eu pego todo objeto da classe (acho q deve fica pesado p caramba)
    
    if nome_categoria:
        produtos = produtos.filter(categoria__nome=nome_categoria) #If vem antes do context caso a regra seja aplicada
    context = {"produtos": produtos}

    

    return render(request, "loja.html", context)

def ver_produto(request, id_produto, id_cor=None):
    tem_estoque = False
    cor = {}
    tamanho = {}
    produto = Produto.objects.get(id = id_produto) #no django toda classe tem o par ID criado automaticamente
    itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0) #Acesso a todos os parametros do objeto
    if id_cor:
            itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0, cor__id = id_cor) #cada coluna tem o msm id? ou casda coluna tem um id
            tamanho = set(item.tamanho for item in itens_estoque) 
    if len(itens_estoque) > 0:
        tem_estoque = True
        cor = [item.cor for item in itens_estoque] # tem varias cores (azul, azul, preto, branco, branco)
        cor = set(cor) #ordena por ordem crescente numeros e não aceita duplicadas ou seja (azul, preto, branco)
        

    
    context = {"produto": produto, "itens_estoque": itens_estoque, "tem_estoque":tem_estoque, "cores": cor, "tamanhos": tamanho}
    return render (request, "ver_produto.html", context)

def carrinho(request):
    return render(request, "carrinho.html")

def checkout(request):
    return render(request, "checkout.html")

def minha_conta(request):
    return render(request, "usuario/minha_conta.html")

def login(request):
    return render(request, "usuario/login.html") #estão na pasta usuario
