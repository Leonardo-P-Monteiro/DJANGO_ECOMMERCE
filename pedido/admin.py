from django.contrib import admin
from .models import Pedido, ItemPedido

# Register your models here.

class ItemPedidosInLine(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = ItemPedidosInLine,

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    pass

