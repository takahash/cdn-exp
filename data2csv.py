#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import csv

# f = open('./result/cdn_cloudfront_4m.json', 'r')
f = open('./result/cdn_cloudfront_10m.json', 'r')
# f = open('./result/cdn_cloudfront_2m.json', 'r')
# f = open('./result/cdn_azure_2m.json', 'r')
# f = open('./result/origin_2m.json', 'r')
data = json.load(f)

# f = open('./result/cdn_cloudfront_4m.csv', 'w')
f = open('./result/cdn_cloudfront_10m.csv', 'w')
# f = open('./result/cdn_cloudfront_2m.csv', 'w')
# f = open('./result/cdn_azure_2m.csv', 'w')
# f = open('./result/origin_2m.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(data)
f.close()
