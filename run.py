#! /usr/bin/env python3
import os
import requests
import json
url='http://35.225.248.24/feedback/'
original_path = "/data/feedback/"
keys = ['title','name','date','feedback']
served_files = os.listdir(original_path)
upload = {}

for file in served_files:
    with open(original_path+file) as feed:
        i=0
        for line in feed:
            print(line)
            upload[keys[i]]=line.rstrip('\n')
            i+=1
        response=requests.post(url, data=upload)
