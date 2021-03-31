from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome =  models.CharField('Nome', max_length=50)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade_estoque = models.IntegerField('Quantidade em Estoque')
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome: ', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)