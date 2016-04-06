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

print "import json"
execfile("../modules/isogeo-api-py-minsdk/isogeo_sdk.py")
print "print json.dumps(objekt)"


# connectBDD = ETAPE 1 #
# Permet de sortir sur le terminal le futur fichier .json avec les commandes nécessaires pour le convertir #