#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 3
    Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
    Calcule o total em segundos.
"""

dias=int(raw_input("Digite a quantidade de dias? "))
horas=int(raw_input("Digite a quantidade de horas? "))
minutos=int(raw_input("Digite a quantide de minutos? "))
segundos=int(raw_input("Digite a quantidade de segundos? "))

s_dias=dias*86400 # ou 24*3600
s_horas=horas*3600
s_minutos=minutos*60
total=s_dias+s_horas+s_minutos+segundos

print "Total é igua a ", int(total)




