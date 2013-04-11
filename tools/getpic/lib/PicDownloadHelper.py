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

    def saveTag(self):
        tag = 'tag1';
        condition  = "name = '" + tag + "'"
        table = 'term'
        select = self.mysqlHelper.select(table, condition)

        data = {"name":"tag1","type":"tag"}
        # self.mysqlHelper.insert("term", data)


  
def test():
    savePath = '/tmp'
    dbConfig = { "user":"root","pw":"1234", "host":"localhost", "db":"520xmn"}
    picDownload = PicDownloadHelper(savePath,dbConfig)
    picDownload.saveTag()

if __name__ == '__main__':
    test()  
