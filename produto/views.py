from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Listar Produtos')
    
class DetlheProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes do Produto')
    
class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao Carrinho')
    
class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do Carrinho')
    
class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')
    
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')