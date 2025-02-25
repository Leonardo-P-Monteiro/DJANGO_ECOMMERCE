def formata_preco(var):
    return f'R$ {var:.2f}'.replace('.', '.')

def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])

def cart_totals(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional') 
            if item.get('preco_quantitativo_promocional') 
            else item.get('preco_quantitativo') 
            for 
            item in carrinho.values()
        ]
    )
    
    # return sum([item.get('preco_quantitativo_promocional') if item.get('preco_quantitativo_promocional') else item.get('preco_quantitativo') in i from carrinho.values()])