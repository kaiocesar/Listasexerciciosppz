#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 7
    Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
"""

celsius=float(raw_input("Digite a temperatura em graus celsius? "))

#print 'Celsius: ',str(celsius),'º\n\rFahrenheit: ',str(9*celsius/5+32),'F'

print 'Celsius: %s\n\rFahrenheit: %s F ' % (str(celsius), str(9*celsius/5+32))


