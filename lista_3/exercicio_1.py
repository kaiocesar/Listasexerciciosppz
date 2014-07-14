#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exercico 1 - Lista 3 do Curso Python para Zumbis
    Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
    seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota=-1
while (nota < 0 or nota > 10):
    nota = float(raw_input("Digite sua nota: "))

    if nota < 0 or nota > 10:
        print "Nota inválida"
    else:
        print "Nota válida"



