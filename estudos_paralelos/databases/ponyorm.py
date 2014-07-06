#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exemplo de utilização do simpatico ORM Pony http://ponyorm.com/
    a. Utilizarei o mesmo dump de MySQL

    Para mais informações acesse a documentação do ORM
    https://github.com/ponyorm/pony/blob/orm/doc/database.txt
    http://initd.org/psycopg/docs/module.html#psycopg2.connect
    http://doc.ponyorm.com/database.html?highlight=mysql
"""

from pony.orm import *

# conexão MySQL
db = Database()
db.bind('mysql', host='127.0.0.1', user='root', passwd='', db='blog')

sql_debug(True)







#conexão PostgreSQL
# db.bind('postgres', user='tom', passwd='tom', db='jerry')

