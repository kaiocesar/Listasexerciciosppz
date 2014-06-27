#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 4
    Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
    porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

salario=float(raw_input("Digite o valor do salario ? "))
porc_aumento=float(raw_input("Digite o valor da porcentagem de aumento? "))

sal_liquido=salario+(salario*(porc_aumento/100))

print 'Salario R$ %5.2f\n\rPorcentagem de aumento: %d\n\rSalario liquido R$ %5.2f' % (salario, porc_aumento, sal_liquido)
