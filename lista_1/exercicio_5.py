#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author: Kaio Cesar
    Email: tecnico.kaio@gmail.com

    Exercicio da Lista I exercícios 5
    Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
"""

preco=float(raw_input("Preço da mercadoria em reais? "))
desconto=float(raw_input("Percentual desconto? ")) / 100

#print "Valor do produto R$",str(preco)," \n\rDesconto: ",str(desconto),"%\n\rValor total R$",str(preco-(preco*desconto))

print 'Valor do produto R$%5.2f\n\rDesconto: %d\n\rValor total R$%5.2f' % (preco, desconto, (preco-(preco*desconto)))
