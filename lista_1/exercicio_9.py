#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 9
    Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
    usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
    sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""
from decimal import *

qtd_km=int(raw_input("Quantidade de Km percorridos? "))
qtd_dias=int(raw_input("Quantidade de dias de aluguel? "))

getcontext().prec = 2

preco= Decimal((qtd_dias*60.00)+(qtd_km*0.15))

print " Você deve R$ %5.2f" % (preco)