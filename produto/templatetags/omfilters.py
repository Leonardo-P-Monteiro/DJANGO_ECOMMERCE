from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(var):
    return f'R$ {var:.2f}'.replace('.', ',')

@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)

@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)