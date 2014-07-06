#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exemplo de conexão com uma base PostgreSQL
    1- Certifique-se que a biblioteca psycopg2 está instalada em sua máquina
        sudo yum -y install python-psycopg2

    Para mais informações http://www.tutorialspoint.com/postgresql/postgresql_python.htm
                          http://initd.org/psycopg/docs/module.html#psycopg2.connect
"""
import os
import psycopg2
import urlparse


try:
    connect = psycopg2.connect(database='blog', user='postgres', password='', host='127.0.0.1', port='5432')
    cur = connect.cursor()
    selectall(cur)
except:
    print 'Could connect database.'
    quit()



def selectall(cr):
    cr.execute("SELECT * FROM posts")
    rows = cr.fetchall()
    return rows

