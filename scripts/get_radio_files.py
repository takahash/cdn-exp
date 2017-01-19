#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import sys
import random
import time
import json

def download():
    times = 5
    path = "files_2m/"
    url = "http://ichikawa-lab-exp.westus.cloudapp.azure.com/" + path
    result = []
    
    for count in range(1, times):
        group_dl_start = time.time()
        sec = random.randint(1, 450)
        each_result = {}
        for num in range(5):
            start = time.time()
            file_name = "{0}-{1}-{2}".format(count, sec, sec + num)
            urllib.urlretrieve(url + str(sec), "./" + path + file_name)
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
            each_result.update({file_name: elapsed_time})
        result.append(each_result)
    f = open("output.json", "w")
    json.dump(result, f)

if __name__ == "__main__":
    download()
 