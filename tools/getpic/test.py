import sys; 
if not "./lib" in sys.path:
    sys.path.append("./lib") 

import HtmlHelper
import UrlParser

# mysql =MySQLHelper('localhost','root','123456')
# mysql.selectDb('520xmn')
# insert_data = {
# 	'src' : 'testsrc2e',
# 	'path' : 'path',
# 	'file_name' : 'one.jpg'
# }
# mysql.insert('pic',insert_data)
# ret = mysql.queryAll("select count(*) from pic where 1")
# print ret

def testGetLink(src, savePath): 
	allLinks = []
	allPics = []
	allLinks.append(src)
	htmlHelpr = HtmlHelper.HtmlHelper()
	urlParser = UrlParser.UrlParser()
	countLinks = 0
	countPics = 0

	# html = htmlHelpr.gGetHtml(src)
	# urlParser.feed(src, html)
	# links = urlParser.getLinks()
	# imgs = urlParser.getPics()
	# for img in imgs:
	# 	fileName = htmlHelpr.gGetPicName(img)
	# 	htmlHelpr.gDownloadWithFilename(img, savePath, fileName)
	for src in allLinks :
		if countLinks>20 :
			break
		if countPics > 600 :
			break
		countLinks = countLinks + 1
		print "begin url: " + src
		html = htmlHelpr.gGetHtml(src)
		urlParser.feed(src, html)
		links = urlParser.getLinks()
		imgs = urlParser.getPics()
		for link in links:
			if link not in allLinks:
				allLinks.append(link)

		for img in imgs:
			if img not in allPics:
				countPics = countPics + 1
				allPics.append(img)
				fileName = htmlHelpr.gGetPicName(img)
				htmlHelpr.gDownloadWithFilename(img, savePath, fileName)

		

	print "has download " + countLinks + "  pages and " + countPics +" pics"


# test()
src = "http://girl.pare.cn/page/4"
savePath = 'I:\\kerwin_www\\tmp\\'
testGetLink(src, savePath)
