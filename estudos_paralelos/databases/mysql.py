#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Conexão do Python com banco de dados Mysql
    1- instalar o modulo python-mysql
        sudo yum -y install MySQL-python.x86_64
    2- declara o modulo "MySQLdb"
    3- Sobe o dump mysql.sql
"""
import MySQLdb
from datetime import date

connect = MySQLdb.connect(host='127.0.0.1',user='root', passwd='', db='blog')

cur = connect.cursor()

# LISTAGEM DOS DADOS
cur.execute("SELECT * FROM posts")

for post in cur.fetchall():
    if (len(post)):
        if (post[4]=='1'):
            print 'Id: %s' % (post[0])
            print 'Ttitle: %s' % (post[1])
            print 'Body: %s' % (post[2])
            print 'Created at: %s' % (post[3])
            print '\n\r'

# INSERT
query = 'INSERT INTO posts (title, body, created_at, status) VALUES ("PROXIMO TITULO POST","CORPO DO POST BLABABLA",""'
cur.execute