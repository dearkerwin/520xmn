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
            item = self.mysqlHelper.save('term',data)
            if item > 0 :
                return self.mysqlHelper.getLastInsertId()
            else :
                raise Exception("save tag faildure")

    """ 获取一个图片的ID"""
    def getPicId(self, src):
        data = {"src":src}
        item = self.mysqlHelper.find('pic', data, "id")
        if  'id' in item:
            return item['id']
        else :
            return 0

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

  
def test():
    savePath = '/tmp'
    dbConfig = { "user":"root","pw":"123456", "host":"localhost", "db":"520xmn"}
    picDownload = PicDownloadHelper(savePath,dbConfig)
    data = {'src':"http:11", "path":"/tmp"}
    ret = picDownload.savePic(data)
    print ret

if __name__ == '__main__':
    test()  
