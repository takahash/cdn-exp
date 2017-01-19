#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import sys
import random
import time
import json

def download():
    times = 30
    
    cdn = "origin/"
    # cdn = "cdn_azure/"
    # cdn = "cdn_cloudfront/"
    # cdn = "cdn_cloudflare/"
    
    path = "files_2m/"
    # path = "files_10m/"
    # path = "files_20m/"
    # path = "files_50m/"
    
    url = "http://ichikawa-lab-exp.westus.cloudapp.azure.com/" + path
    # url = "http://ichikawa-lab-exp1.azureedge.net" + path
    # url = "http://dv12b46anbdab.cloudfront.net" + path
    # url = "http://ichikawa-lab-exp.tkhskn.me" + path
    result = []
    
    for count in range(1, times+1):
        group_dl_start = time.time()
        sec = random.randint(1, 450)
        each_result = {}
        for num in range(50):
            start = time.time()
            file_name = "{0}-{1}-{2}".format(count, sec, sec + num)
            urllib.urlretrieve(url + str(sec), "./" + cdn + path + file_name)
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
            each_result.update({file_name: elapsed_time})
        result.append(each_result)
    f = open("./{0}{1}output.json".format(cdn, path), "w")
    json.dump(result, f)

if __name__ == "__main__":
    download()
 
