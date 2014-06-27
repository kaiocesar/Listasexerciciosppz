#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 10
    Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
    quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
    perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
    total de dias.
"""

from time import *
from datetime import datetime

qtd_cigarros_dia=int(raw_input("Qual a quantidade de cigarros por dia ? "))
qtd_anos_fumados=int(raw_input("Qual a quantidade de anos que você já fumou ? "))

vida_por_dia=qtd_cigarros_dia*600
vida_por_ano=qtd_anos_fumados*365
resto=vida_por_ano*vida_por_dia

#tempo_perdido=datetime.fromtimestamp(resto)
#datetime.fromtimestamp(mktime(resto))

print 'Desses %d anos fumados. Fumando %d cigarro(s) por dia. Você já perdeu %f s de vida perdidos.' % (qtd_anos_fumados, qtd_cigarros_dia, resto)
