from django.shortcuts import render, redirect
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
    cor_selecionada = None
    produto = Produto.objects.get(id = id_produto) #no django toda classe tem o par ID criado automaticamente
    itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0) #Acesso a todos os parametros do objeto
    if id_cor:
            itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0, cor__id = id_cor) #quantidade_GT é do própio DJANGO.GT --> Greather Than
            tamanho = [ item.tamanho for item in itens_estoque ]
            cor_selecionada = CorProduto.objects.get(id = id_cor)
    if len(itens_estoque) > 0:
        tem_estoque = True
        cor = [item.cor for item in itens_estoque] # tem varias cores (azul, azul, preto, branco, branco)
        cor = set(cor) #ordena por ordem crescente numeros e não aceita duplicadas ou seja (azul, preto, branco)

    context = {"produto": produto, "tem_estoque":tem_estoque, "cores": cor, "tamanhos": tamanho, "cores_selecionadas":cor_selecionada}
    return render (request, "ver_produto.html", context)

def carrinho(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente

    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)

    context = {"itens_pedido": itens_pedido, "pedido":pedido}
    return render(request, "carrinho.html", context)

def checkout(request):
    return render(request, "checkout.html")

def minha_conta(request):
    return render(request, "usuario/minha_conta.html")

def login(request):
    return render(request, "usuario/login.html") #estão na pasta usuario

def adicionar_carrinho(request, id_produto):
    if request.method == "POST" and id_produto:
        dados = request.POST.dict()
        tamanho = dados.get("tamanho")
        cor = dados.get("cor")
        nome_cor = CorProduto.objects.filter(id = cor).first()
        print(nome_cor)
        print(cor)
        print(tamanho)
        ### Criar pedido ou pegar pedido em aberto ####
        ### Pegar cliente
        if not tamanho:
            return redirect('loja')
        return redirect("carrinho")
    else:
        return redirect("loja") #metodo django redirect leva em consideração NAME atribuido em urls.py

    
