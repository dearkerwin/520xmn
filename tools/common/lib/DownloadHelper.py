# -*- coding: utf-8 -*-
"""
download heper 提供功能：
    获取指定url的html, 下载html的代码
eg:
    helpr = DownloadHelper('http://web-proxy.oa.com:8080')
    url = 'http://www.baidu.com' 
    html = helpr.gGetHtmlLines(url)

version 1.0
author kerwin
"""
import urllib2, urlparse, httplib
import os
import Image
class DownloadHelper():
    def __init__(self, proxy='' ):
        self.proxy = ''
        if proxy != '':
            self.proxy = proxy
            self.setProxy(proxy)

    """ 设置全局的proxy"""
    def setProxy(self, proxy):
        self.proxy = proxy
        if self.proxy != '' and self.proxy :
            proxy = urllib2.ProxyHandler({'http': self.proxy})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)


    def __urlopen(self, url):
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
        return urllib2.urlopen(request, timeout=10)

    """get html src,return lines[]"""
    def gGetHtmlLines(self,url):
        if url==None : return
        # if not self.httpExists(url): return 
        try:
            page = self.__urlopen(url)   
            html = page.readlines()
            page.close()
            return html
        except:
            print "gGetHtmlLines() error!"
            return

    """get html src,return string"""
    def gGetHtml(self,url):
        if url==None : return " "
        # if not self.httpExists(url): return  " "
        try:
            page = self.__urlopen(url)   
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




def test():
    helpr = DownloadHelper('http://web-proxy.oa.com:8080')
    # helpr.setProxy('http://web-proxy.oa.com:8080')
    url = 'http://ifxoxo.com'
    
    html = helpr.gGetHtml(url)
    print html
    

    
if __name__ == '__main__':
    test()  
