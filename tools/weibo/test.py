# _*_ coding: utf-8 _*_

import os
import sys
import weibo
import webbrowser
import json

APP_KEY = '2047884174'
MY_APP_SECRET = '3c6086543774f0d025e85e358ec204c0'
# REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'
REDIRECT_URL = 'http://ifxoxo.com'
#这个是设置回调地址，必须与那个”高级信息“里的一致

#请求用户授权的过程
client = weibo.APIClient(APP_KEY, MY_APP_SECRET)

authorize_url = client.get_authorize_url(REDIRECT_URL)

#print authorize_url
#authorize_url = 'https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//ifxoxo.com&response_type=code&client_id=2047884174'

#打开浏览器，需手动找到地址栏中URL里的code字段
webbrowser.open(authorize_url)

#将code字段后的值输入控制台中
code = raw_input("input the code: ").strip()

#获得用户授权
request = client.request_access_token(code, REDIRECT_URL)


#token_url = 'https://api.weibo.com/oauth2/access_token?client_id=2047884174&client_secret=3c6086543774f0d025e85e358ec204c0&grant_type=authorization_code&redirect_uri=http%3A//ifxoxo.com&code=4e32a0203336de8f4eb442a95af57490'

#保存access_token ,exires_in, uid
access_token = request.access_token
expires_in = request.expires_in
uid = request.uid
print access_token
print expires_in
print uid

#设置accsess_token，client可以直接调用API了
client.set_access_token(access_token, expires_in)

#get_results = client.statuses__mentions()
#get_results = client.frientdships__friends__ids()
#get_results = client.statuses__user_timeline()
#get_results = client.statuses__repost_timeline(id = uid)
#get_results = client.search__topics(q = "笨NANA")
get_results = client.statuses__friends_timeline()
print "************the type of get_results is : "
print type(get_results)
#print get_results[0][0]['text']
get_statuses = get_results.__getattr__('statuses')
print type(get_statuses)
print get_statuses[0]['text']

json_obg = json.dumps(get_results)
print type(json_obg)
#resultsdic = json.load(json_obg)

print uid

# get_json = json.dumps(client.statuses__user_timeline())
#decodejson = json.loads(get_results)
#print decodejson

#file = open("result.txt", "w")
#file.write(decodejson)
#file.close()
print "*************OK**********"