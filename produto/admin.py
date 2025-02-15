from django.contrib import admin
from .models import Produto, Variacao

# Register your models here.

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 3

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    
    list_display = 'nome', 'descricao_curta', 'get_preco_formatado', \
                    'get_preco_promocional_formatado',

    inlines = VariacaoInLine,
    prepopulated_fields = {
        'slug':('nome',)
    } 



@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    ...