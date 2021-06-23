#! /usr/bin/env python3
import os
import requests

def sendinfo():
        for rev in reviews:
                response = requests.post("http://34.121.229.35/feedback/",data = rev)
                print(response.request.body)
                if not response.ok:
                        raise Exception("GET failed with status code {}".format(response.status_code))


directory = "/data/feedback"
reviews = []
rev = 0
for filename in os.listdir(directory):
        filepath = directory +"/"+ filename
        if filename.endswith(".txt"):
            with open(filepath,"r") as review:
                dict={}
                pos = 0
                for line in review:
                    line=line.strip("\n")
                    if pos == 0:
                        dict["title"] = line
                    elif pos == 1:
                        dict["name"] = line
                    elif pos == 2:
                        dict["date"] = line
                    elif pos == 3:
                        dict["feedback"] = line
                    pos+=1
        rev+=1
        dict_cop = dict.copy()
        reviews.append(dict_cop)
print(reviews[1])
