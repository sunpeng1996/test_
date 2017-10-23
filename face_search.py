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
if len(sys.argv) != 3:
	print "请输入合法参数 待检测图片地址 [image_address] 本地图片库文件夹地址 [face_dir_path]"
	os._exit(0)

access_token = '24.a169d6ce40151ee8b022651b2052e104.2592000.1507689696.282335-10121479'

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"

request_url = request_url + "?access_token=" + access_token

image_address = str(sys.argv[1])
face_dir_path = str(sys.argv[2])

hit = False

# 二进制方式打开图文件
f = open(image_address, 'rb')
img1 = base64.b64encode(f.read())
for image in os.listdir(face_dir_path):
	temp_image_f = open(face_dir_path+image,'rb')
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
	    	break

if hit == False:
	print "找不到该人"














