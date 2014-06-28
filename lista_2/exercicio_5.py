#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exercicio 5 - Lista 2 do curso Python para Zumbis
    Escrecer um programa que receba 3 valores e processo o maior e menor numeros, e os exiba na tela.
"""

a = float(raw_input('Digite um valor para A? '))
b = float(raw_input('Digite um valor para B? '))
c = float(raw_input('Digite um valor para C? '))

media = (a + b + c) / 3

# Maior
if (a > media):
    maior = 'A é o maior'
elif (b > media):
    maior = 'B é o maior'
else:
    maior = 'C é o maior'

# Menor
if (a < b and a < c):
    menor = 'A é o menor'
elif (b < c):
    menor = 'B é o menor'
else:
    menor = 'C é menor'

print maior , menor
