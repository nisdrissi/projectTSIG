#!/usr/bin/python
# -*- coding: utf-8 -*-

#LIBRAIRIES#

# Standard library
import base64
from collections import Counter
import socket
import locale
import logging
from math import ceil
from sys import platform as opersys

# 3rd party library
import os
import json
import requests
import subprocess
import fileinput

# Permet d'enregistrer la sortie terminal de connectBDD
with open('sortieISOGEO.py','w+') as output:
    subprocess.call(["python", "./connectBDD.py"], stdout=output);

#Remplace l'erreur 4 du premier fichier de sortie
f = open('sortieISOGEO.py','r')
filedata = f.read()
f.close()

newdata = filedata.replace("4","objekt =", 1)

f = open('sortieISOGEOV2.py','w')
f.write(newdata)
f.close()

subprocess.call(["python", "sortieISOGEOV2.py"], shell=None)


# Permet d'enregistrer la sortie finale en .json #
with open('sortieISOGEO_final.json','w+') as output:
    subprocess.call(["python", "./sortieISOGEOV2.py"], stdout=output);
print "REUSSI"


os.remove('sortieISOGEO.py')
os.remove('sortieISOGEOV2.py')