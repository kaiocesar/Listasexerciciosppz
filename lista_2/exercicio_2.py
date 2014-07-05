#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @author Kaio Cesar
    Exercicio 2 - Lista 2 do curso Python para Zumbis 2013
    Determine se um ano é bissexto.
"""

ano = int(raw_input('Digite o valor do ano ? '))
bissexto = ano % 4

if (bissexto == 0):
    print 'Ano bissexto'
else:
    print 'Não é bissexto'