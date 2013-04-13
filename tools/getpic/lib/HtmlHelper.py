# -*- coding: utf-8 -*-
"""
html heper 提供功能：
    获取指定url的html，根据url获取文件名，根据url获取图片名，根据url下载文件
eg:
    savePath='/tmp'
    img = 'http://pic.pare.cn/p3/2013-04-01-16-13-59_j.jpg'  
    htmlHelpr = HtmlHelper()
    fileName = htmlHelpr.gGetPicName(img)
    htmlHelpr.gDownloadWithFilename(img, savePath, fileName) #下载该图片

version 1.0
author kerwin
"""
import urllib, httplib, urlparse
import os
class HtmlHelper():

    """根据url下载文件，文件名参数指定"""
    def gDownloadWithFilename(self,url,savePath,fileName):
        if savePath[ len(savePath) - 1 ] != '/':
            savePath = savePath + "/"
        try:
            if not os.path.isfile(savePath + fileName) :
                print 'download ' + fileName 
                urlopen=urllib.URLopener()
                fp = urlopen.open(url)
                data = fp.read()
                fp.close()
                file=open(savePath + fileName,'w+b')
                file.write(data)
                file.close()
            else :
                print 'ingore : ' + fileName 
            return True
        except IOError:
            print "download error!"+ url
            return False

    """根据url获取文件名"""
    def gGetFileName(self,url):
        if url==None: return None
        if url=="" : return ""
        arr=url.split("/")
        return arr[len(arr)-1]

    """根据url获取图片名"""
    def gGetPicName(self,url):
        if url==None: return None
        if url=="" : return ""
        fileName = self.gGetFileName(url)
        arr=fileName.split(".")
        format = arr[len(arr)-1]
        formats = ['gif','jpg','jpeg','bmp','png','GIF','JPG','JPEG','BMP','PNG']
        if format in formats:
            return fileName
        else:
            return fileName+".jpg"

    """get html src,return lines[]"""
    def gGetHtmlLines(self,url):
        if url==None : return
        if not self.httpExists(url): return 
        try:
            page = urllib.urlopen(url)   
            html = page.readlines()
            page.close()
            return html
        except:
            print "gGetHtmlLines() error!"
            return

    """get html src,return string"""
    def gGetHtml(self,url):
        if url==None : return " "
        if not self.httpExists(url): return  " "
        try:
            page = urllib.urlopen(url)   
            html = page.read()
            page.close()
            return html
        except:
            print "gGetHtml() error!"
            return " "

    """判断 url exists or not """
    def httpExists(self,url):
        host, path = urlparse.urlsplit(url)[1:3]
        if ':' in host:
            # port specified, try to use it
            host, port = host.split(':', 1)
            try:
                port = int(port)
            except ValueError:
                print 'invalid port number %r' % (port,)
                return False
        else:
            # no port specified, use default port
            port = None
        try:
            connection = httplib.HTTPConnection(host, port=port)
            connection.request("HEAD", path)
            resp = connection.getresponse( )
            if resp.status == 200:       # normal 'found' status
                found = True
            elif resp.status == 302:     # recurse on temporary redirect
                found = httpExists(urlparse.urljoin(url,resp.getheader('location', '')))
            else:                        # everything else -> not found
                print "Status %d %s : %s" % (resp.status, resp.reason, url)
                found = False
        except Exception, e:
            print e.__class__, e, url
            found = False
        return found

    """ 获取url的host """
    def getHost(self, url):
        if url==None: return None
        if url=="" : return ""
        host = urlparse.urlsplit(url)[1]
        return host