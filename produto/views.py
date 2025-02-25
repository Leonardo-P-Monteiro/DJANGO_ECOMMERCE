from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models
from django.contrib import messages
from pprint import pprint

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 6
    
class DetlheProdutos(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):

        
        # Este trecho é apenas para limpar o carrinho durante os testes.
        # if self.request.session.get('carrinho'):
        #     del self.request.session['carrinho']
        #     self.request.session.save()
        #     pprint(self.request.session.get('carrinho', 'Carrinho zerado.'))

        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(self.request, 
                           'Produto não existe.')

            return redirect(http_referer)
        
        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        produto = variacao.produto
        variacao_estoque = variacao.estoque
        
        produto_id = produto.pk
        produto_nome = produto.nome
        variacao_nome = variacao.nome
        variacao_id = variacao_id
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem.name if produto.imagem else '' # Isso é um operador ternário.

        if variacao_estoque < 1:
            messages.error(self.request, 'Estoque insuficiente.')

            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        
        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
            
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no \
                    produto "{produto_nome}". Adicionamos apenas \
                    {variacao_estoque}x ao seu carrinho.'
                )
            
                quantidade_carrinho = variacao_estoque


            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = \
                                quantidade_carrinho * preco_unitario
            carrinho[variacao_id]['preco_quantitativo_promocional'] = \
                                quantidade_carrinho * preco_unitario_promocional

        else:

            carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id, 
                'preco_unitario': preco_unitario, 
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
                }
        print('VISTA DO ADICIONAR CARRINHO')
        pprint(self.request.session['carrinho'])
        self.request.session.save()
        

        messages.success(
            self.request, 
            f'O produto {variacao_nome} foi adicionado ao carrinho. \
                Quantidade no carrinho: {carrinho[variacao_id]['quantidade']}'
                         )

        return redirect(http_referer)

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        
        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')
        
        if not variacao_id:
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['carrinho']:
            return redirect(http_referer)
        
        carrinho = self.request.session['carrinho'][variacao_id]

        

        messages.success(self.request,
                         f'O item "{carrinho['produto_nome']}" foi removido \
                             do seu carrinho.')

        
        pprint(self.request.session['carrinho'])
        del self.request.session['carrinho'][variacao_id]

        self.request.session.save()

        return redirect(http_referer)

class Carrinho(View):
    def get(self, *args, **kwargs):
        pprint(self.request.session['carrinho'])
        return render(self.request, 'produto/carrinho.html')
        
    
class ResumoDaCompra(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')

