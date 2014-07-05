#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Exemplo de conexão com uma base PostgreSQL
    1- Certifique-se que a biblioteca psycopg2 está instalada em sua máquina
        sudo yum -y install python-psycopg2

    Para mais informações http://www.tutorialspoint.com/postgresql/postgresql_python.htm

"""

import psycopg2

connect = psycopg2.connect(database='jerry', user='tom', password='tom', host='127.0.0.1', port='5432')

