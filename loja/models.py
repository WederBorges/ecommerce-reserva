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
    
    def __str__(self):
        return str(self.nome)

class Tipo(models.Model): # Tipo -> Camisa, Camiseta, Calça, Bermuda, Sapato, etc...    
    nome = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return str(self.nome)
    
class Produto(models.Model): #
    imagem = models.ImageField(max_length=400, null=False, blank=True) 
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2) # decimal_places -> 1000000000,00 termina com 2 casas decimais
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL) # models.SET_NULL -> Se uma Categoria for excluída o campo do produto fica vazio.

    def __str__(self):
        return f"{self.nome} - R$:{self.preco} - CATEGORIA: {self.categoria} - TIPO: {self.tipo} "
    
class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=10, null=True, blank=True)
    quantidade = models.IntegerField(default=0)

class Endereco(models.Model):
    cep = models.CharField(max_length=500, null=True, blank=True)
    rua = models.CharField(max_length=500, null=True, blank=True) 
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=30, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL) #cliente ID ou Nome eu acho
    finalizado = models.BooleanField(default=False) #Campo boleeano define se o pedido foi finalizado ou pendente
    cod_pedido = models.CharField(max_length=200, null=True, blank=True) #codigo do pedido -> cada item tem um pedido
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL) #end cadastro associado ao cliente
    data_finalizacao = models.DateTimeField(null=True, blank=True ) #data finalizacao do pedido

class ItensPedido(models.Model):  
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)
    item_estoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)

class Banner(models.Model):
    imagem = models.ImageField(blank=True, null=True) 
    link_destino = models.CharField(max_length=400, blank=True, null=True)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        status = "Ativo" if self.ativo == True else "Inativo" #Mostra ativo se True, inativo se Else.

        return f"{self.link_destino} - Ativo: {status}"