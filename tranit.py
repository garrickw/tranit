#!/usr/bin/env python
# _*_ coding:utf8 _*_


#This is a tiny application using for translate word or sentence from chinese to English , or from English to Chinese
#
#steps:
#1 get the querry token from the command line
#2  make the  full url 
#3 requests the url and get the json
#4 get the result from the json

##api  example:
# http://fanyi.youdao.com/openapi.do?keyfrom=<keyfrom>&key=<key>&type=data&doctype=json&version=1.1&q=good
# {
#     "errorCode":0
#     "query":"good",
#     "translation":["好"], // 有道翻译
#     "basic":{ // 有道词典-基本词典
#         "phonetic":"gʊd"
#         "uk-phonetic":"gʊd" //英式发音
#         "us-phonetic":"ɡʊd" //美式发音
#         "explains":[
#             "好处",
#             "好的"
#             "好"
#         ]
#     },
#     "web":[ // 有道词典-网络释义
#         {
#             "key":"good",
#             "value":["良好","善","美好"]
#         },
#         {...}
#     ]
# }

import sys
import requests
import json

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print "Usage: tranit 'queryword or a sentence' (without quote)."
		exit(1)

	querry = " ".join(sys.argv[1:])
	youdao = "http://fanyi.youdao.com/openapi.do?keyfrom=helloword159&key=540616135&type=data&doctype=json&version=1.1&q={}".format(querry)

	try:
		res = requests.get(youdao);
	except Exception,e:
		print e
	

	jsondata = res.text
	results = json.loads(jsondata)

	if results['translation'][0]:
		print results['translation'][0]
		print '-'*20
	try:
		for explain in   results.get('basic').get('explains'):
			print explain
		print '-'*20
	
		webs= results.get("web")
		print "From web:"
		for each in webs:
			print each['key']+":"
			print "; ".join(each['value'])
	except Exception:
		pass
