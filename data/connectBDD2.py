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

with open('sortieISOGEO.py','w+') as output:
    subprocess.call(["python", "./connectBDD.py"], stdout=output);

f = open('sortieISOGEO.py','r')
filedata = f.read()
f.close()

newdata = filedata.replace("4","objekt =", 1)

f = open('sortieISOGEOV2.py','w')
f.write(newdata)
f.close()

subprocess.call(["python", "sortieISOGEOV2.py"], shell=None)

#connectBDD2 = ETAPE 2 #
# Permet d'enregistrer la sortie terminal de connectBDD
# Permet d'executer la sortie terminal sortieISOGEO.py #