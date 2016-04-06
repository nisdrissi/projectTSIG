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
# import isogeo
import requests
import subprocess
import fileinput


with open('sortieISOGEO_final.json','w+') as output:
    subprocess.call(["python", "./sortieISOGEOV2.py"], stdout=output);
print "REUSSI"


#connectBDD3 = ETAPE 3 #
# Permet d'enregistrer la sortie finale en .json #