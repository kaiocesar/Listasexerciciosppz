#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Exercício 5 - Lista 3 do Curso Python Para Zumbis
    Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
"""

numero = raw_input('Entre com um número? ')
if (float(numero) > -1):
    print numero[::-1]
else:
    print 'Entrada inválida.'