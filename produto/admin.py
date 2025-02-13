from django.contrib import admin
from .models import Produto, Variacao

# Register your models here.

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 3

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    
    inlines = VariacaoInLine,
    prepopulated_fields = {
        'slug':('nome',)
    } 



@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    ...