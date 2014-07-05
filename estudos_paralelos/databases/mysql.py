#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Conexão do Python com banco de dados Mysql
    1- instalar o modulo python-mysql
        sudo yum -y install MySQL-python.x86_64
    2- declara o modulo "MySQLdb"
    3- Sobe o dump mysql.sql

    Para mais informações consulte a documentação do MySQLdb
    http://mysql-python.sourceforge.net/MySQLdb.html
"""

import MySQLdb
import time


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
dataUx = time.localtime()
datahoje ='%s-%02d-%02d 00:00:00' % (dataUx.tm_year, dataUx.tm_mon, dataUx.tm_mday)

query = "INSERT INTO posts (id,title, body, created_at, status) VALUES (null,'alor on danse teste PROXIMO TITULO POST','CORPO DO POST BLABABLA','%s','1'); " % (datahoje)

if (cur.execute(query)==1):
    print 'Dados inseridos com sucesso.\n\rLast id: %s' % (connect.insert_id())
else:
    print 'Erro ao adicionar os dados.'

connect.commit()



# UPDATE
query = "UPDATE posts SET title = '%s' where id = %d " % ('Titulo alterado do blog',1)
up_ok = cur.execute(query)

if (up_ok==1):
    print 'Linha atualizada com sucesso.'
else:
    print 'Falha na atualização'

connect.commit()


# DELETE
query = "DELETE FROM posts where id = %d " % (12)
del_ok = cur.execute(query)

if (del_ok==1):
    print 'Linha deletada com sucesso.'
else:
    print 'Falha na deleção'

connect.commit()


# Por fim fechamos a conexão
connect.close()