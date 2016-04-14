#!/usr/bin/python
# -*- coding: utf-8 -*-

# TUTORIEL : http://zetcode.com/db/postgresqlpythontutorial/ #
# COMMANDES PSQL : http://docs.postgresql.fr/8.0/app-psql.html #

import psycopg2
import psycopg2.extras
import sys

#### RECUPERATION DES FORMATS#####

con = None

try:
    
    con = psycopg2.connect("dbname='chimn' user='postgres'") #Connexion à la BDD
    
    nt_cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    nt_cur.execute("SELECT nom FROM preferenceformat WHERE activated = 'True'") #requête SQL formats
        
    firstResultFormat = nt_cur.fetchmany(6)
        
    print firstResultFormat
    
    resultFormat = firstResultFormat


#### RECUPERATION DES SRS#####
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT code FROM preferencesrs WHERE preferencesrs.activate='True'") #requête SQL SRS
        
    firestResultSRS = cursor.fetchmany(3)


    print firestResultSRS
    resultSRS = firestResultSRS

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:
    
    if con:
        con.close()