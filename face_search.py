# encoding:utf-8
import base64
import urllib
import urllib2
import os
import sys
import json
'''
人脸查找之识别接口
调用方式: python face_search.py 待查找图片 一个文件夹路径(保存用户已经存储的人的图片，命名为人名,方便返回人名)
'''
access_token = '24.d2fe5c5740aad24864b5fcd920195d16.2592000.1511328623.282335-10121479'

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"

SAVED_PATH = "saved_face"

request_url = request_url + "?access_token=" + access_token

hit = False

def face_search(image_address):
	f = open(image_address, 'rb')
	img1 = base64.b64encode(f.read())
	for image in os.listdir(SAVED_PATH):
		temp_image_f = open(SAVED_PATH+image,'rb')
		img_temp = base64.b64encode(temp_image_f.read())
		params = {"images":img1 + ',' + img_temp}
		params = urllib.urlencode(params)
		request = urllib2.Request(url=request_url, data=params)
		request.add_header('Content-Type', 'application/x-www-form-urlencoded')
		response = urllib2.urlopen(request)
		content = response.read()
		if content:
		    content = json.loads(content)
		    if float(content['result'][0]['score']) > 80:
		    	print "配对成功,此人为:"+image
		    	hit = True
		    	return "配对成功,此人为:"+image
		    	break
		# 二进制方式打开图文件
		if hit == False:
			print "找不到该人"
			return None















