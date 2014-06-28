#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Author: Kaio Cesar
    Exercicio 1 - Lista de exercicios 2 (Curso Python para Zumbis)
    Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
    um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""
from math import sqrt


a=float(raw_input("Valor para A? "))
b=float(raw_input("Valor para B? "))
c=float(raw_input("Valor para C? "))

# h^2=co^2+ca^2
# |b-c| < a & < b+c
# |a-c| < b & < a+c
# |a-b| < c & < a+b

if ( ( sqrt(b-c) < a) and (a < (b+c))):
    if ( ( sqrt(a-c) < b) and (b < (a+c)) ):
        if ( ( sqrt(a-b) < c ) and (c < a+b) ):
            print 'Its all right.'
