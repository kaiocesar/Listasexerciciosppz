#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 6
    Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
    esperada para a viagem.
"""
import datetime

distancia=float(raw_input("Qual a distancia a percorrer? "))
velocidade=float(raw_input("Qual a velocidade média (km/h)? "))

tempo=(distancia*3600/velocidade)

print 'Tempo de viagem em horas é ',str(datetime.timedelta(seconds=tempo))


