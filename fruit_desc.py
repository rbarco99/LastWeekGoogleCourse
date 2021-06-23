#!/usr/bin/env python3
import os
import requests
'''PROCESS THE .TXT FILES AND CONVER THE DATA INTO A DICTIONARY FOR SEND TO THE FRUITS WEBPAGE '''
def sendinfo(fr):
        response = requests.post("http://35.194.0.165/fruits/",data = fr)
        print(response.request.body)
        if not response.ok:
            raise Exception("GET failed with status code {}".format(response.status_code))  


dir = "./supplier-data/descriptions/"
items = ["name", "weight","description","image_name"]
for filename in os.listdir(dir):
        filepath = dir + filename
        if filename.endswith(".txt"):
            with open(filepath,"r") as fruits:
                fruit_direc = {}
                cont = 0
                for line in fruits:
                    line=line.strip("\n")
                    if cont == 1:
                        line = ''.join([i for i in line if i.isdigit()])
                        line = int(line)
                    fruit_direc[items[cont]] = line
                    cont +=1
                fruit_direc["image_name"] = filename.replace(".txt",".jpeg")
        print(fruit_direc)
        sendinfo(fruit_direc)




