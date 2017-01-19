#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import sys
import random
import time
import json

def download():
    size = 10   # セグメントファイルのサイズ(MB)
    sec_size = size / 2
    times = 100  # 試行回数
    path = "files_10m/"
    
    cdn = "origin/"
    # cdn = "cdn_azure/"
    # cdn = "cdn_cloudfront/"
    # cdn = "cdn_cloudflare/"
    
    url = "http://ichikawa-lab-exp.westus.cloudapp.azure.com/" + path
    # url = "http://ichikawa-lab-exp1.azureedge.net/" + path
    # url = "http://dv12b46anbdab.cloudfront.net/" + path
    # url = "http://ichikawa-lab-exp.tkhskn.me/" + path
    result = []

    for count in range(1, times+1):
        sec = random.randint(1, 450)
        if (sec % sec_size) == 0:
            start_file = sec
            end_file = sec + 20
        else:
            start_file = (sec / sec_size) + 1
            end_file = start_file + ((20 / sec_size) + 1)
        each_result = {}
        for num in range(start_file, end_file + 1):
            start = time.time()
            file_name = "{0}-{1}-{2}".format(count, sec, num)
            urllib.urlretrieve(url + str(num), "./{0}{1}{2}".format(cdn, path, file_name))
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
            each_result.update({file_name: elapsed_time})
        result.append(each_result)
    f = open("./{0}{1}output.json".format(cdn, path), "w")
    json.dump(result, f)

if __name__ == "__main__":
    download()
 
