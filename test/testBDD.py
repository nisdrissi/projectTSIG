#!/usr/bin/python
# -*- coding: utf-8 -*-

# TUTORIEL : http://zetcode.com/db/postgresqlpythontutorial/ #
# COMMANDES PSQL : http://docs.postgresql.fr/8.0/app-psql.html #

import psycopg2
import psycopg2.extras
import sys


con = None

try:
    
    con = psycopg2.connect("dbname='chimn' user='postgres'")
    
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM preferenceformat WHERE activated = 'True'")
    
    while True:
        
        row = cursor.fetchone()
        
        if row == None:
            break
        
        print row[0], row[1]


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:
    
    if con:
        con.close()


con = None

try:
    
    con = psycopg2.connect("dbname='chimn' user='postgres'")
    
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM preferencesrs WHERE preferencesrs.activate='True'")
    
    while True:
        
        row = cursor.fetchone()
        
        if row == None:
            break
        
        print row[0], row[1]


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:
    
    if con:
        con.close()