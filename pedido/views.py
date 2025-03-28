from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib import messages
from produto.models import Variacao
from utils import utils
from .models import Pedido, ItemPedido
from copy import deepcopy

# Create your views here.

class Pagar(View):
    
    """
    É nessa view que iríamos inserir os métodos de pagamento ou até mesmo 
    o cálculo de frete (o correto é ser exibido também na página de anúncio 
    do produto) em uma situação real. 
    """

    template_name = 'pedido/pagar.html'
    
    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Você precisa fazer login para \
                           continuar.')
            
            return redirect('perfil:criar')
            

        if not self.request.session.get('carrinho'):
            messages.error(self.request, 'Carrinho está vazio.')

            return redirect('produto:lista')

        carrinho = self.request.session.get('carrinho')
        carrinho_variacao_id = [v for v in carrinho.keys()]
        bd_variacoes = list(
            Variacao.objects.select_related('produto')
            .filter(id__in= carrinho_variacao_id)
        )

        for variacao in bd_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qtd_carrinho = carrinho[vid]['quantidade']
            preco_unt = carrinho[vid]['preco_unitario']
            preco_unt_promo = carrinho[vid]['preco_unitario_promocional']



            if estoque == 0:
                
                messages.warning( self.request,
                                f'O item {carrinho[vid]['produto_nome']} \
                                foi removido do carrinho por falta de estoque')

                del carrinho[vid]

                self.request.session.save()

                return redirect('produto:carrinho')

            if estoque < qtd_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = preco_unt * estoque
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * \
                    preco_unt_promo

                messages.warning(self.request,
                            'Alguns produtos do seu carrinho estão com '
                            'estoque insuficiente e tivemos que reduzir suas '
                            'quantidades. Verifique as quantidades dos seus '
                            'produtos novamente.')
                
                self.request.session.save()

                return redirect('produto:carrinho')
        
        qtd_total_carrinho = utils.cart_total_qtd(carrinho)
        valor_total_carrinho = utils.cart_totals(carrinho)

        pedido = Pedido(
            usuario = self.request.user,
            total = valor_total_carrinho,
            qtd_total = qtd_total_carrinho,
            status = 'C'
        )

        pedido.save()

        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido = pedido,
                    produto = i['produto_nome'],
                    produto_id = i['produto_id'],
                    variacao = i['variacao_nome'],
                    variacao_id = i['variacao_id'],
                    preco = i['preco_quantitativo'],
                    preco_promocional = i['preco_quantitativo_promocional'],
                    quantidade = i['quantidade'],
                    imagem = i['imagem'],
                ) for i in carrinho.values()
            ]
        )


        carrinho_pedido = deepcopy(carrinho) # Cópia por precaução.
        del self.request.session['carrinho']

        contexto = {}


        # return render(self.request, self.template_name, contexto)
        return redirect('pedido:lista')

class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar Pedido')

class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')

class Lista(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista de Pedidos')