# -*- coding: utf-8 -*-
"""
分析html代码，获取html代码上的 超链接 和 图片链接
eg:
    url = "http://www.baidu.com"
    html = '<body><a href="http://hi.baidu.com/217a007/item/45134fb6465150d484dd79c0" ></body>'
    parser = UrlParser()
    parser.feed(url,html)
    links = parser.getLinks()

version 0.2
author kerwin
"""
import re

class UrlParser():
    def __init__ (self):
        self.data = "";
        self.url = "";

    """设置当前页面的Url和html代码""" 
    def feed(self,url,data):
        if url==None : url = ""
        if data==None : url = ""
        self.url = url;
        self.data = data;
    
    """获取所有超链接的url""" 
    def getLinks(self):
        
        rex = r'''<a(\s*)(.*?)(\s*)href(\s*)=(\s*)(["'\s]*)([^"']+?)(["'\s]+)(.*?)>'''
        url = re.findall(rex, self.data, re.S|re.I)
        links = []
        for u in url:
            link = self.gGetAbslLink(u[6])
            if link not in links:
                links.append(link)
        return links

    """获取所有的图片的地址"""
    def getPics(self):
        rex = r'''<img(\s*)(.*?)(\s*)src(\s*)=(\s*)(["'\s]*)([^"']+?)(["'\s]+)(.*?)>'''
        url = re.findall(rex, self.data, re.S|re.I)
        img = []
        for u in url:
            src = self.gGetAbslLink(u[6])
            if src not in img:
                img.append(src)
        return img

    """根据link，得到link的绝对地址"""
    def gGetAbslLink(self,link):
        link = link.strip()
        if self.url==None or link == None : return 
        if self.url=='' or link=='' : return self.url 
        addr = '' 
        if link[0] == '/' : 
            #如果是根目录链接
            addr = self.gGetHttpAddr() + link 
        elif len(link)>3 and link[0:4] == 'http':
            #如果是http链接
            addr =  link 
        elif len(link)>2 and link[0:2] == '..':
            #如果是上上级目录的链接
            addr = self.gGetHttpAddrFatherAssign(link)
        else:
            #如果是上级目录的链接
            addr = self.gGetHttpAddrFather() + link 

        return addr 

    """当前url取主站地址"""
    def gGetHttpAddr(self):
        if self.url== '' : return ''
        arr = self.url.split("/")
        return arr[0]+"//"+arr[2]

    """取当前url上级目录"""
    def gGetHttpAddrFather(self):
        if self.url=='' : return ''
        arr = self.url.split("/")
        addr = arr[0]+'//'+arr[2]+ '/'
        if len(arr)-1>3 :
            for i in range(3,len(arr)-1):
                addr = addr + arr[i] + '/'
        return addr

    """如果是当前url的上上级目录，根据当前url 获取link的绝对地址"""
    def gGetHttpAddrFatherAssign(self,link):
        if self.url=='' : return ''
        if link=='': return ''
        linkArray=link.split("/")
        urlArray = self.url.split("/")
        partLink =''
        partUrl = ''
        for i in range(len(linkArray)):        
            if linkArray[i]=='..': 
                numOfFather = i + 1    #上级数
            else:
                partLink = partLink + '/'  + linkArray[i]
        for i in range(len(urlArray)-1-numOfFather):
            partUrl = partUrl + urlArray[i] 
            if i < len(urlArray)-1-numOfFather -1 : 
                partUrl = partUrl + '/'
        return  partUrl + partLink

