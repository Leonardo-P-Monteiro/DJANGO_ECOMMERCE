from django.template import Library

register = Library()

@register.filter
def formata_preco(var):
    return f'R$ {var:.2f}'.replace('.', ',')