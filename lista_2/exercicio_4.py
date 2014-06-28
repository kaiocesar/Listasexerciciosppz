#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Author: Kaio Cesar
    Exercicio 4 - Lista de exercicios 2 (Curso Python para Zumbis)
    Faça um Programa que leia três números e mostre o maior deles.
"""
def maior_numer():
    a=float(raw_input('Digite um valor para A? '))
    b=float(raw_input('Digite um valor para B? '))
    c=float(raw_input('Digite um valor para C? '))

    media=(a+b+c)/3

    if (a > media):
        print "\"A\" é o maior valor"
    elif (b > media):
        print "\"B\" é o maior valor"
    else:
        print "\"C\" é o maior valor"


maior_numer()