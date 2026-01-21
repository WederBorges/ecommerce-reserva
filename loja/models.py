from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model): # id populado automaticamente pelo Django
    nome = models.CharField(max_length=80, null=True, blank=True)
    email = models.CharField(max_length=80, null=True, blank=True)
    telefone = models.CharField(max_length=80, null=True, blank=True)
    id_sessao = models.CharField(max_length=80, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) 
### Obs null=True -> banco aceita vazio ---- blank=True -> Formulário aceita em branco.


class Categoria(models.Model): # Categoria -> Feminino, Masculino, Kids, etc...
    nome = models.CharField(max_length=80, null=True, blank=True)
    

class Tipo(models.Model): # Tipo -> Camisa, Camiseta, Calça, Bermuda, Sapato, etc...    
    nome = models.CharField(max_length=80, null=True, blank=True)

class Produto(models.Model): #
    imagem = models.CharField(max_length=400, null=False, blank=True) 
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2) # decimal_places -> 1000000000,00 termina com 2 casas decimais
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL) # models.SET_NULL -> Se uma categoria for excluída o campo do produto fica vazio.
    