#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exercicio 2 - Lista de exercicios 3 do Curso Python para Zumbis
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
    nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = raw_input('Digite o nome de usuário ? ')
senha = nome

while(senha == nome):
    senha = raw_input('Digite a senha do usuário ? ')
    if (senha == nome):
        print 'A senha não pode ser igual ao nome de usuario\n\rPor favor '