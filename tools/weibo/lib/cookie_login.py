#coding=utf8

import urllib2
import re

"""
Login to Sina Weibo with cookie
"""

COOKIE = 'SINAGLOBAL=638810985255.9865.1359941983537; sso_info=ln%3D377418118%2540qq.com%26nick%3Dkerwin%26uid%3D1875510074; login_sid_t=215418aea4261b52632ce4063bc9fe2e; USRUG=usrmdins41456; _s_tentry=-; Apache=7933069767896.086.1378960108633; ULV=1378960108660:151:12:6:7933069767896.086.1378960108633:1378870440359; USRHAWB=usrmdins312_158; __utma=182865017.1525663355.1378982954.1378982954.1378982954.1; __utmc=182865017; __utmz=182865017.1378982954.1.1.utmcsr=weibo.com|utmccn=(referral)|utmcmd=referral|utmcct=/dearkelvin; myuid=1875510074; UOR=weibo.com,weibo.com,login.sina.com.cn; SUE=es%3D8be452ee3e1c7a8743578cc9c49757b7%26ev%3Dv1%26es2%3D6409165aaba1cf53a963adbcc91695e2%26rs0%3DQNsmhJQ2G1m9acoxnWh7LvEi03gMMnXGFoYzTBzw6EkodFVRFWLbjO4FKUxgmFmY%252FwLOYQIbhLcmTMlQUo%252BOfSqcm%252BQ8DS6qj25cHf5hF6w%252BbwIPwuXR1hd8Gy70skMmdE2i9tpMhKIkB%252Bzg7aF94%252FNqEg3jwdR93GUK6MygRMo%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1378988830%26et%3D1379075230%26d%3Dc909%26i%3Da6d4%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D3764447374%26name%3D10218664%2540qq.com%26nick%3D%25E6%2588%2591%25E7%259C%259F%25E7%259A%2584%25E4%25B8%258D%25E4%25BC%259A%25E8%25AE%25B2%25E7%25AC%2591%25E8%25AF%259D%26fmp%3D%26lcp%3D; SUS=SID-3764447374-1378988830-JA-4lz1q-bd3e00c50dcd4534732c5eb82ce9ed16; ALF=1381580830; SSOLoginState=1378988830; un=10218664@qq.com; wvr=5; SinaRot_wb_r_topic=17' #fill with your weibo.com cookie
HEADERS = {"cookie": COOKIE}
need_proxy = 1

def test_login():
    url = 'http://weibo.com'
    req = urllib2.Request(url, headers=HEADERS)
    text = _urlopen(req).read()
    print text

    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(text)
    print r
    if r:
        print r.group(1)

def _urlopen(req):
    global need_proxy;
    if need_proxy:
        proxy_support = urllib2.ProxyHandler({'http': 'http://web-proxy.oa.com:8080'})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    try:
        return urllib2.urlopen(req)
    except:
        print "urlopen failded: " + req

if __name__ == '__main__':
    test_login()
