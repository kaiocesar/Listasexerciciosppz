#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exercico 2 - Lista 3 do Curso Python para Zumbis
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
    nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

username = raw_input("Digite o nome de usuário? ")
password = username

while password == username:
    password = raw_input("Digite a senha de usuario? ")
    if password == username:
        print "A senha não pode ser igual ao nome de usuário, por favor "
    else:
        print "Obrigado."