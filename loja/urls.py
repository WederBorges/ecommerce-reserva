from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"), #homepage -> carrega dominio padrão
    path('loja/', loja, name="loja"),  
    path('loja/<str:nome_categoria>/', loja, name="loja"),
    path('produto/<str:id_produto>/', ver_produto, name="ver_produto"),
    path('produto/<str:id_produto>/<int:id_cor>/', ver_produto, name="ver_produto"),
    path('minhaconta/', minha_conta, name="minha_conta"),
    path('carrinho/', carrinho, name="carrinho"),
    path('login/', login, name="login"), 
    path('checkout/', checkout, name="checkout")
] 

### path("URL que aparece no navegaor, funcao executada em python, nome interno da url")