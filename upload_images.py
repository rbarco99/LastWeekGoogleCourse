#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
dict = "./supplier-data/images/"
for filename in os.listdir(dict):
    if filename.endswith(".jpeg"):
        path = dict + filename
        with open(path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

"""Este programa permite subir los archivos jpeg a la pagina wb con django"""
