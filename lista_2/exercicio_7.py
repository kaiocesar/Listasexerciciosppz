#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    @autho Kaio Cesar
    Exercicios 7 Lista de exercícios do curso Python para Zumbis
    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
    ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
    em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
    compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
"""

area_pintar  = float(raw_input('Por favor informe o tamanho da área em m² ? '))
qtd_latas = area_pintar / 3
print 'Quantidade de latas é igual a %d\n\rValor total R$ %.2f ' % (qtd_latas,(qtd_latas*18.00))


