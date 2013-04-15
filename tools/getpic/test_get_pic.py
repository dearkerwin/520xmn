# -*- coding: utf-8 -*-
"""
some function by metaphy,2007-04-03,copyleft
version 0.2
"""
import urllib, httplib, urlparse
import re
import random
import os

############################################################
class UrlParser():
    def __init__ (self):
        self.data = "";
        self.url = "";

    """设置当前页面的Url和html代码""" 
    def feed(self,url,data):
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
                print link
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

##############################################


class HtmlHelper():

    """根据url下载文件，文件名参数指定"""
    def gDownloadWithFilename(self,url,savePath,fileName):
        #参数检查，现忽略
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
        except IOError:
            print "download error!"+ url

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
        if url==None : return
        if not self.httpExists(url): return 
        try:
            page = urllib.urlopen(url)   
            html = page.read()
            page.close()
            return html
        except:
            print "gGetHtml() error!"
            return

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

##############################################


"""judge url exists or not,by others"""
def httpExists(url):
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

"""get html src,return lines[]"""
def gGetHtmlLines(url):
    if url==None : return
    if not httpExists(url): return 
    try:
        page = urllib.urlopen(url)   
        html = page.readlines()
        page.close()
        return html
    except:
        print "gGetHtmlLines() error!"
        return
"""get html src,return string"""
def gGetHtml(url):
    if url==None : return
    if not httpExists(url): return 
    try:
        page = urllib.urlopen(url)   
        html = page.read()
        page.close()
        return html
    except:
        print "gGetHtml() error!"
        return

"""根据url获取文件名"""
def gGetFileName(url):
    if url==None: return None
    if url=="" : return ""
    arr=url.split("/")
    return arr[len(arr)-1]

"""生成随机文件名"""
def gRandFilename(type):
    fname = ''
    for i in range(16):
        fname = fname + chr(random.randint(65,90))
        fname = fname + chr(random.randint(48,57))
    return fname + '.' + type
"""根据url和其上的link，得到link的绝对地址"""
def gGetAbslLink(url,link):
    if url==None or link == None : return 
    if url=='' or link=='' : return url 
    addr = '' 
    if link[0] == '/' : 
        addr = gGetHttpAddr(url) + link 
    elif len(link)>3 and link[0:4] == 'http':
        addr =  link 
    elif len(link)>2 and link[0:2] == '..':
        addr = gGetHttpAddrFatherAssign(url,link)
    else:
        addr = gGetHttpAddrFather(url) + link 

    return addr 

"""根据输入的lines，匹配正则表达式，返回list"""
def gGetRegList(linesList,regx):
    if linesList==None : return 
    rtnList=[]
    for line in linesList:
        matchs = re.search(regx, line, re.IGNORECASE)
        if matchs!=None:
            allGroups = matchs.groups()
            for foundStr in allGroups:
                if foundStr not in rtnList:
                    rtnList.append(foundStr)
    return rtnList
"""根据url下载文件，文件名参数指定"""
def gDownloadWithFilename(url,savePath,file):
    #参数检查，现忽略
    try:
        if not os.path.isfile(savePath + file) :
            print 'download ' + file 
            urlopen=urllib.URLopener()
            fp = urlopen.open(url)
            data = fp.read()
            fp.close()
            file=open(savePath + file,'w+b')
            file.write(data)
            file.close()
        else :
            print 'ingore : ' + file 
    except IOError:
        print "download error!"+ url
        
"""根据url下载文件，文件名自动从url获取"""
def gDownload(url,savePath):
    #参数检查，现忽略
    fileName = gGetFileName(url)
    #fileName =gRandFilename('jpg')
    gDownloadWithFilename(url,savePath,fileName)
    
        
"""根据某网页的url,下载该网页的jpg"""
def gDownloadHtmlJpg(downloadUrl,savePath):
    print "begin url: " + downloadUrl
    lines= gGetHtmlLines(downloadUrl)
    regx = r"""src\s*="?(\S+)\.jpg"""
    lists =gGetRegList(lines,regx)
    if lists==None: return 
    for jpg in lists:
        jpg = gGetAbslLink(downloadUrl,jpg) + '.jpg'
        gDownload(jpg,savePath)
   ###     print gGetFileName(jpg)
"""根据url取主站地址"""
def gGetHttpAddr(url):
    if url== '' : return ''
    arr=url.split("/")
    return arr[0]+"//"+arr[2]
"""根据url取上级目录"""
def gGetHttpAddrFather(url):
    if url=='' : return ''
    arr=url.split("/")
    addr = arr[0]+'//'+arr[2]+ '/'
    if len(arr)-1>3 :
        for i in range(3,len(arr)-1):
            addr = addr + arr[i] + '/'
    return addr

"""根据url和上级的link取link的绝对地址"""
def gGetHttpAddrFatherAssign(url,link):
    if url=='' : return ''
    if link=='': return ''
    linkArray=link.split("/")
    urlArray = url.split("/")
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

"""根据url获取其上的相关htm、html链接，返回list"""
def gGetHtmlLink(url):
    #参数检查，现忽略
    rtnList=[]
    lines=gGetHtmlLines(url)
    regx = r"""href="?(\S+)\.html"""
    for link in gGetRegList(lines,regx):
        link = gGetAbslLink(url,link) + '.html'
        if link not in rtnList:
            rtnList.append(link)
            print link
    return rtnList

"""根据url，抓取其上的jpg和其链接htm上的jpg"""
def gDownloadAllJpg(url,savePath):
    #参数检查，现忽略
    gDownloadHtmlJpg(url,savePath)
    #抓取link上的jpg
    links=gGetHtmlLink(url)
    # for link in links:
    #     gDownloadHtmlJpg(link,savePath)

"""test"""
def test():
    u='http://girl.pare.cn/'
    # u = 'http://girl.pare.cn/6744.html'
    save='I:\\kerwin_www\\tmp\\'
    print 'download pic from [' + u +']'
    print 'save to [' +save+'] ...'
    # gDownloadHtmlJpg(u,save)
    gDownloadAllJpg(u,save)
    print "download finished"


######################################################################



"""根据url获取其上的相关链接，返回list"""
def gGetHtmlLink_new(url):
    #参数检查，现忽略
    rtnList=[]
    # html=gGetHtml(url)
    html = "<a href=' stockings ' class='tag-link-30' title='44 个话题' style='font-size: 12px;'>"

    # rex = r'''<a(\s*)(.*?)(\s*)href(\s*)=(\s*)(["'\s]*)([^"']+?)(["'\s]+)(.*?)>'''
    # url = re.findall(rex, html, re.S|re.I)
    # print url
    print "has download html content"
    Parser = UrlParser()
    Parser.feed(url,html)
    Parser.getLinks()

    # regx = r"""href="?(\S+)\.html"""
    # allLinks = gGetRegList(lines,regx)
    # for link in allLinks :
    #     link = gGetAbslLink(url,link) + '.html'
    #     if link not in rtnList:
    #         rtnList.append(link)
    #         print link
    # return rtnList

def testGetLink():
     # u='http://girl.pare.cn/page/2'
     # gGetHtmlLink_new(u)
    src = "http://girl.pare.cn/page/2"
    savePath = 'I:\\kerwin_www\\tmp\\'
    htmlHelpr = HtmlHelper()
    urlParser = UrlParser()
    html = htmlHelpr.gGetHtml(src)
    urlParser.feed(src, html)
    imgs = urlParser.getPics()
    for img in imgs:
        fileName = htmlHelpr.gGetPicName(img)
        htmlHelpr.gDownloadWithFilename(img, savePath, fileName)



# test()
testGetLink()
