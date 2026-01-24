from django.shortcuts import render
from .models import *
# Create your views here.

def homepage(request):
    return render(request,"homepage.html") #paginas do site

def loja(request):
    produtos = Produto.objects.all() #aqui eu pego todo objeto da classe (acho q deve fica pesado p caramba)
    context = {"produtos": produtos}
    return render(request,"loja.html", context)

def carrinho(request):
    return render(request,"carrinho.html")

def checkout(request):
    return render(request,"checkout.html")

def minha_conta(request):
    return render(request,"usuario/minha_conta.html")

def login(request):
    return render(request,"usuario/login.html") #estão na pasta usuario
