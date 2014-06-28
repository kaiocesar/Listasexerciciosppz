#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @autho Kaio Cesar
    Exercício 6 - Lista II de exercício - Curso Python para Zumbis
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
    e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
    quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
    descontos e o salário líquido, conforme a tabela abaixo:
    a. + Salário Bruto : R$
    b. - IR (11%) : R$
    c. - INSS (8%) : R$
    d. - Sindicato ( 5%) : R$
    e. = Salário Liquido : R$
"""

salario_hora = float(raw_input('Qual o valor por hora trabalhada ? '))
qtd_horas_trab = int(raw_input('Qual a quantidade de horas trabalhadas no mes ? '))

salario_bruto = salario_hora * qtd_horas_trab
salario_bruto = salario_bruto - (salario_bruto * 0.11)
salario_bruto = salario_bruto - (salario_bruto * 0.08)
salario_bruta = salario_bruto - (salario_bruto * 0.05)

print 'Salario liquido R$ %5.2f' % (salario_bruto)