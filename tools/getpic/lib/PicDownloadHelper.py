# -*- coding: utf-8 -*-
"""
pic heper 提供功能：
    把pic 存到本地，把tag存到数据库等

version 1.0
author kerwin
"""
import MySQLHelper
import HtmlHelper

class PicDownloadHelper():

    def __init__(self,savePath, dbConfig):
        self.savePath=savePath
        self.dbConfig = dbConfig
        self.mysqlHelper = self.getDb()
        self.htmlHelper = HtmlHelper.HtmlHelper()
        

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

    """ 获取一个tag的ID，如果tag不存在，则存入数据库再返回ID"""
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
        for tagId in tagIds:
            data = {'pic_id': picID, 'term_id':tagId}
            relation = self.mysqlHelper.find('pic_term_relation', data)
            if len(relation) == 0:
                #没有数据，进行保存
                self.mysqlHelper.save('pic_term_relation', data)


    """ 保存一个item"""
    def saveItem(self, item):
        pic = item[0]
        tags = item[1]
        picSrc = pic["src"]
        picPath = pic["path"]
        picName = self.htmlHelper.gGetPicName(picSrc)
        picData = {"src":picSrc, "path":picPath, "file_name": picName}
        if self.getPicId(picData) > 0:
        #图片已经存在, 跳过
            return 0;
        else:
            #保存图片
            if self.htmlHelper.gDownloadWithFilename(picSrc,picPath,picName)
                #保存到数据库
                picId = self.savePic(pic)
                if picId > 0 :
                    #图片保存成功，保存标签
                    tagIds = []
                    for tag in tags:
                        tagIds.append( self.getTagId(tag) )
                    self.savePicTagRelation(picId, tagIds)
                    return True
                else :
                    return False



  
def test():
    savePath = '/tmp'
    dbConfig = { "user":"root","pw":"123456", "host":"localhost", "db":"520xmn"}
    picDownload = PicDownloadHelper(savePath,dbConfig)
    pic = {'src':"http:baidu.c1om/1.jpg", "path":savePath}
    tag = ['tag12355','tag12334','tag12556']
    item = [pic,tag]
    ret = picDownload.saveItem(item)
    print ret

if __name__ == '__main__':
    test()  
