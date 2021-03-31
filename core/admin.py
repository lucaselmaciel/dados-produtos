from django.contrib import admin

# Register your models here.
from .models import Produtos,Cliente

class MostrarProduto(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque')

class MostrarCliente(admin.ModelAdmin):
    list_display= ('nome', 'sobrenome', 'email')

admin.site.register(Produtos, MostrarProduto)
admin.site.register(Cliente, MostrarCliente)