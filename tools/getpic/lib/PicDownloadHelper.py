# -*- coding: utf-8 -*-
"""
pic heper 提供功能：
    把pic 存到本地，把tag存到数据库等

version 1.0
author kerwin
"""
import MySQLHelper
import HtmlHelper
import PicHelper
import os, time


class PicDownloadHelper():

    def __init__(self,savePath,thumbPath, dbConfig):
        self.savePath = savePath + self.getChildPath( savePath )
        self.thumbPath = thumbPath + self.getChildPath( thumbPath )
        self.childPath = self.getChildPath( savePath )  #用于保存的子目录名
        self.dbConfig = dbConfig
        self.mysqlHelper = self.getDb()
        self.htmlHelper = HtmlHelper.HtmlHelper()
        self.picHelper = PicHelper.PicHelper()
        
        # lock = threading.Condition()

    """ 根据当前的时间，返回一个用于保存图片的子目录，如果不存在，则创建"""
    def getChildPath (self, save_path):
        year = time.localtime()[0]
        month = time.localtime()[1]
        path =  str(year) + "/" + str(month) + "/"
        year_path = save_path + str(year) + "/"
        month_path = save_path + str(year) + "/" + str(month) + "/"

        if not os.path.isdir( year_path ):
            os.mkdir(year_path)
        if not os.path.isdir( month_path ):
            os.mkdir(month_path)
        return path


    """ 获取一个数据库操作类"""
    def getDb(self):
        user = self.dbConfig['user']
        password = self.dbConfig['pw']
        host = self.dbConfig['host']
        db = self.dbConfig['db']
        if self.dbConfig.has_key('unix_socket'):
            unix_socket = self.dbConfig['unix_socket']
            mysqlHelper = MySQLHelper.MySQLHelper(host,user,password,db=db, unix_socket = unix_socket)
        else :
            mysqlHelper = MySQLHelper.MySQLHelper(host,user,password,db=db)
        return mysqlHelper

    """ 
        获取一个tag的ID，如果tag不存在，则存入数据库再返回ID
        @param string tag :一个标签名
        @return int tag的ID
    """
    def getTagId(self, tag):
        data = {"name":tag}
        item = self.mysqlHelper.find('term', data, "id")
        if  'id' in item:
            return item['id']
        else :
            #没有数据，进行保存
            item = self.mysqlHelper.save('term',data)
            if item > 0 :
                return self.mysqlHelper.getLastInsertId()
            else :
                raise Exception("save tag faildure")


    """ 获取一个图片的ID"""
    def getPicId(self, data):
        # data = {"src":src}
        item = self.mysqlHelper.find('pic', data, "id")
        if  'id' in item:
            return item['id']
        else :
            #没有数据，进行保存
            return 0

    """ 保存一个图片, """
    def savePic(self, data):
        check = False
        if isinstance(data, ( dict )):
            if 'src' in data and 'path' in data :
                check = True

        if check:
            ret = self.mysqlHelper.save('pic',data)
            if ret > 0:
                return self.mysqlHelper.getLastInsertId()
            else :
                raise Exception("save pic faildure")
        else:
            raise Exception("save pic faildure: data is wrong")

        return 0

    """ 保存一个图片和 tag 的关系"""
    def savePicTagRelation(self, picID, tagIds):
        check = 0
        for tagId in tagIds:
            data = {'pic_id': picID, 'term_id':tagId}
            relation = self.mysqlHelper.find('pic_term_relation', data)
            if len(relation) == 0:
                #没有数据，进行保存
                if self.mysqlHelper.save('pic_term_relation', data) > 0  :
                    check = check + 1
        return check == len(tagIds)


    """ 保存一个host"""
    def saveHost(self, host):
        data = {"host":host, "status":"disable"}
        relation = self.mysqlHelper.find('host', data)
        if len(relation) == 0:
            #没有数据，进行保存
            self.mysqlHelper.save('host', data)        

    """ 
        保存一个item 
        @param list item 一个包含pic 和 tag 的list
        @return：int code 返回状态码
                    -1 = 参数错误
                    0 = 图片下载失败
                    1 = 图片下载，图片信息保存到数据库失败
                    2 = 图片信息保存成功，标签保存失败
                    3 = 都成功
                    4 = 图片已经存在，忽略
    """
    def saveItem(self, item):
        #检查参数
        if len(item) != 2 or 'src' not in item[0] :
            return -1
        pic = item[0]
        tags = item[1]

        findPicData = {"src":pic['src']}
        # print "find :" + pic['src']
        if self.getPicId(findPicData) > 0:
        #图片已经存在, 跳过
            # print "break: " + pic['src']
            return 4;
        else:

            # print "save: " + pic['src']
            #初始化 picData
            picData = {}.fromkeys(['src','path','file_name','title','remark','postfix','width','height'],'NULL')
            for p in pic:
                picData[p] = pic[p]

            #获取file_name 和 postfix
            picData['file_name'] = self.htmlHelper.gGetPicName( pic["src"])
            picData['path'] = self.childPath
            picData['postfix'] = os.path.splitext(picData['file_name'])[1]

            if(picData['postfix'] == '.gif'): 
                print "ignore gif "
                return 0;

        
            #准备保存图片
            if self.htmlHelper.gDownloadWithFilename(picData['src'], self.savePath, picData['file_name']):
                #生成宽度=260 缩略图
                if not self.picHelper.createWidthThumb(self.savePath, picData['file_name'], self.thumbPath, 260):
                    return 0;
                
                #准备保存pic数据到数据库
                picData['width'],  picData['height'] = self.picHelper.getImageSize(self.savePath,picData['file_name'])
                picId = self.savePic(picData)
                if picId > 0 :
                    #图片保存成功，保存标签
                    tagIds = []
                    for tag in tags:
                        tagIds.append( self.getTagId(tag) )
                    if self.savePicTagRelation(picId, tagIds):
                        #都成功
                        return 3
                    else:
                        #图片信息保存成功，标签保存失败
                        return 2
                else :
                    #图片信息保存到数据库失败
                    return 1
            else:
                #图片下载失败
                return 0
        




  
def test():
    savePath = 'I:/kerwin_www/tmp'
    dbConfig = { "user":"root","pw":"123456", "host":"localhost", "db":"520xmn"}
    picDownload = PicDownloadHelper(savePath,dbConfig)
    pic = {'src':"http://pic.pare.cn/p3/d2013-04-24-17-40-39_4.jpg"}
    tag = ['床','情节','手手','清纯','OL']
    item = [pic,tag]
    ret = picDownload.saveItem(item)
    print ret




if __name__ == '__main__':
    test()  
