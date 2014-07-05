#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    @author Kaio Cesar
    Exercicio 3 - Lista 2 de exercicios do curso Python para Zumbis
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
    seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
    estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
    faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
    variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
    variáveis com o conteúdo ZERO.
"""


kg_peixe = int(raw_input('Digita a quantidade em kg de peixes ? '))
multa = 0;
excesso = 0

if (kg_peixe > 50):
    multa = (kg_peixe - 50) * 4
    excesso = kg_peixe - 50

print "Quantidade de peixes: %d\n\rValor da Multa R$ %.2f\n\rQuantidade excedente: %d" % (kg_peixe, multa, excesso)
