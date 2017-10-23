#coding=utf-8
import urllib, urllib2, sys
import ssl
import json
import sys
import base64
import os
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=aGBdDIL8n5Ve9cmqysU5QcRI&client_secret=rYC9gIxMDf457GhXvUfxvGljhx8ED4bm'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)

if len(sys.argv) != 2:
	print "请输入合法参数 [image_address]"
	os._exit(0)

image_path = str(sys.argv[1])
'''
人脸检测接口
调用方式：python face_detection.py image_path
access_token:有效期30天，由于请求token存在延迟，故写死，注意及时更换。
返回人脸可能性 face_prob, 性别 gender, 是否戴眼镜 glasses
'''
detectUrl = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
# 参数image：图像base64编码，max_face_num：最多处理人脸数目，默认值1，face_fields：包括age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities信息，逗号分隔，默认只返回人脸框、概率和旋转角度\
f=open(image_path,'rb') #二进制方式打开图文件
img=base64.b64encode(f.read())
params = {"max_face_num": 1, "face_fields": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
          "image": img}
params = urllib.urlencode(params)
access_token = '24.d2fe5c5740aad24864b5fcd920195d16.2592000.1511328623.282335-10121479'
detectUrl = detectUrl + "?access_token=" + access_token
request = urllib2.Request(url=detectUrl, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
content = json.loads(content)
content = content['result'][0]

face_prob = content['face_probability']
gender = content['gender']
glasses = content['glasses']


if content:
    print "人脸可能性为:"+str(face_prob)
    print "性别为："+str(gender)
    print "是否戴眼镜："+str(glasses)




