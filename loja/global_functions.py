from .models import ItensPedido, Pedido
def carrinho(request):
    quantidade_adicionada_carrinho = 0
    if request.user.is_authenticated: #verifica se user está logado
        cliente = request.user.cliente
        print(cliente.nome) #pegando dados do cliente atraves da classe Clientes e acessando pelo USER do usuario no request da pagina
    else:
       return {"quantidade_adicionada_carrinho": quantidade_adicionada_carrinho}
    
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        quantidade_adicionada_carrinho += item.quantidade
 #neste caso o 1° cliente é o current user, e o 2° cliente é o cliente.id da tabela Pedidos que seria tipo cliente.id = cliente.id
    return {"quantidade_adicionada_carrinho": quantidade_adicionada_carrinho}

