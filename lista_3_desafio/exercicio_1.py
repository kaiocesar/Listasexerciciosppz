#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import  os

"""
    Exercicio 1 - Lista 3 do curso Python para Zumbis
    Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
    seja inválido e continue pedindo até que o usuário informe um valor válido
"""

num=-1
while (num < 0 or num > 10):
    num = int(raw_input('Entre com um valor valido entre 1 e 10 ?'))
