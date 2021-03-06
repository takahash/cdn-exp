#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib, random, time, json, threading, logging, sys

args = sys.argv
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
size = int(args[1])        	    # セグメントファイルのサイズ(MB)
sec_size = size / 2
times = 50              # 試行回数
period = 30		        # 取得時間(s)
thread_num = 20         # スレッド数

path = "files_{0}m/".format(size)

cdns = [
    "origin/",
    "cdn_azure/",
    "cdn_cloudfront/",
    # "cdn_cloudflare/",
    ]

urls= [
    "http://ichikawa-lab-exp.westus.cloudapp.azure.com/",
    "http://ichikawa-lab-exp1.azureedge.net/",
    "http://dv12b46anbdab.cloudfront.net/",
    # "http://ichikawa-lab-exp.tkhskn.me/",
    ]

cdn = cdns[int(args[2])]
url = urls[int(args[2])] + path

def download(thread_num):
    result = []
    for count in range(1, times+1):
        sec = random.randint(1, 500)
        if (sec % sec_size) == 0:
            start_file = (sec / sec_size) + 1
            end_file = start_file + (period / sec_size)
        else:
            start_file = (sec / sec_size) + 1
            end_file = start_file + ((period / sec_size) + 1) + 1
        each_time = []
        each_file_name = []
        for num in range(start_file, end_file):
            start = time.time()
            file_name = "{0}-{1}-{2}".format(count, sec, num)
            urllib.urlretrieve(url + str(num), "./{0}{1}{2}".format(cdn, path, file_name))
            elapsed_time = time.time() - start
            logging.debug("elapsed_time:{0}".format(elapsed_time) + "[sec]")
            each_time.append(elapsed_time)
            # each_file_name.append(file_name)
        result.append(each_time)
        # result.append(each_file_name)
    logging.debug(str(count) + " times")
    output = open("./{0}{1}output{2}.json".format(cdn, path, thread_num), "w")
    json.dump(result, output)

if __name__ == "__main__":
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=download, args=(i,))
        threads.append(t)
        t.start()
