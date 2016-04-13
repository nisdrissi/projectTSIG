#!/usr/bin/python
# -*- coding: utf-8 -*-
# Doc os.system http://cdn.safe.com/resources/webinar-data/conterra-python-webinar-slides.pdf #

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
with open('sortieBDDformat.py','w+') as output:
    subprocess.call(["python", "./testBDD.py"], stdout=output);

#### SHAPEFILE ####
    if 'SHP' in open('sortieBDDformat.py').read():
        #checker la correspondance format
        if 'RGF93' in open('sortieBDDformat.py').read():
            #lancer le traitement SHP/Lambert93.fmw
            os.system('fme.exe postgis2shape_testLambert93.fmw \
                      --SourceData ANYSOURCE \
                      --DestinationData ANYDEST\
                      --AnyParam ParamValue')
            print "true SHP LAMBERT93"
        if 'WGS84' in open('sortieBDDformat.py').read():
            #lancer le traitement SHP/WGS84.fmw
            print "true SHP WGS84"
        if 'Web Mercator' in open('sortieBDDformat.py').read():
            #lancer le traitement SHP/Web Mercator.fmw
            print "true SHP Web Mercator"
    else:
        print "false" #trouver un moyen de passer au suivant

#### DXF ####
    if 'DXF' in open('sortieBDDformat.py').read():
        #checker la correspondance format
        if 'RGF93' in open('sortieBDDformat.py').read():
            #lancer le traitement DXF/Lambert93.fmw
            print "true DXF LAMBERT93"
        if 'WGS84' in open('sortieBDDformat.py').read():
            #lancer le traitement DXF/WGS84.fmw
            print "true DXF WGS84"
        if 'Web Mercator' in open('sortieBDDformat.py').read():
            #lancer le traitement DXF/Web Mercator.fmw
            print "true DXF Web Mercator"
    else:
        print "false" #trouver un moyen de passer au suivant

#### GML ####
    if 'GML' in open('sortieBDDformat.py').read():
        #checker la correspondance format
        if 'RGF93' in open('sortieBDDformat.py').read():
            #lancer le traitement GML/Lambert93.fmw
            print "true GML LAMBERT93"
        if 'WGS84' in open('sortieBDDformat.py').read():
            #lancer le traitement GML/WGS84.fmw
            print "true GML WGS84"
        if 'Web Mercator' in open('sortieBDDformat.py').read():
            #lancer le traitement GML/Web Mercator.fmw
            print "true GML Web Mercator"
    else:
        print "false" #trouver un moyen de passer au suivant

#### JPEG ####
    if 'JPEG' in open('sortieBDDformat.py').read():
        #checker la correspondance format
        if 'RGF93' in open('sortieBDDformat.py').read():
            #lancer le traitement JPEG/Lambert93.fmw
            print "true JPEG LAMBERT93"
        if 'WGS84' in open('sortieBDDformat.py').read():
            #lancer le traitement JPEG/WGS84.fmw
            print "true JPEG WGS84"
        if 'Web Mercator' in open('sortieBDDformat.py').read():
            #lancer le traitement JPEG/Web Mercator.fmw
            print "true JPEG Web Mercator"
    else:
        print "false" #trouver un moyen de passer au suivant

#### PNG ####
    if 'PNG' in open('sortieBDDformat.py').read():
    #checker la correspondance format
        if 'RGF93' in open('sortieBDDformat.py').read():
            #lancer le traitement PNG/Lambert93.fmw
            print "true PNG LAMBERT93"
        if 'WGS84' in open('sortieBDDformat.py').read():
            #lancer le traitement PNG/WGS84.fmw
            print "true PNG WGS84"
        if 'Web Mercator' in open('sortieBDDformat.py').read():
            #lancer le traitement PNG/Web Mercator.fmw
            print "true PNG Web Mercator"
    else:
        print "false" #trouver un moyen de passer au suivant

#### GeoTIFF ####
    if 'GeoTIFF' in open('sortieBDDformat.py').read():
        #checker la correspondance format
        if 'RGF93' in open('sortieBDDformat.py').read():
            #lancer le traitement GeoTIFF/Lambert93.fmw
            print "true GeoTIFF LAMBERT93"
        if 'WGS84' in open('sortieBDDformat.py').read():
            #lancer le traitement GeoTIFF/WGS84.fmw
            print "true GeoTIFF WGS84"
        if 'Web Mercator' in open('sortieBDDformat.py').read():
            #lancer le traitement GeoTIFF/Web Mercator.fmw
            print "true GeoTIFF Web Mercator"
    else:
        print "false" #trouver un moyen de passer au suivant