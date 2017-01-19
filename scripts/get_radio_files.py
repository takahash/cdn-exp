#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import sys
import random
import time
import json

def download():
    size = 4        	    # セグメントファイルのサイズ(MB)
    sec_size = size / 2
    times = 50              # 試行回数
    period = 20
    
    # path = "files_2m/"
    path = "files_4m/"
    # path = "files_10m/"
    # path = "files_20m/"
    
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
            end_file = sec + (period / sec_size)
        else:
            start_file = (sec / sec_size) + 1
            end_file = start_file + ((period / sec_size) + 1)
        each_time = []
        each_file_name = []
        for num in range(start_file, end_file):
            start = time.time()
            file_name = "{0}-{1}-{2}".format(count, sec, num)
            urllib.urlretrieve(url + str(num), "./{0}{1}{2}".format(cdn, path, file_name))
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
            each_time.append(elapsed_time)
            # each_file_name.append(file_name)
        result.append(each_time)
        # result.append(each_file_name)
	print str(count) + " times"
    f = open("./{0}{1}output.json".format(cdn, path), "w")
    json.dump(result, f)

if __name__ == "__main__":
    download()
