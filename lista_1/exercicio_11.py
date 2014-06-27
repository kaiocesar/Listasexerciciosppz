#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 11
    Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
"""

valor=2**1000000
print '2 ^ 1 milhão tem %d caracteres' % (len(str(valor)))