from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), name='adicionaraocarrinho'),
    path('removerDoCarrinho/', views.RemoverDoCarrinho.as_view(), name='RemoverDoCarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='Carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
    path('<slug:slug>', views.DetlheProdutos.as_view(), name='detalhe'),
] 