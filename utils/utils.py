def formata_preco(var):
    return f'R$ {var:.2f}'.replace('.', '.')

def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])