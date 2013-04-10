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
        self.mysqlHelper = self.get_db()
        


    def get_db():
        user = self.dbConfig['user']
        pw = self.dbConfig['pw']
        host = self.dbConfig['host']
        if self.dbConfig.has_key('unix_socket'):
            unix_socket = self.dbConfig['unix_socket']
            mysqlHelper = MySQLHelper.MySQLHelper(host,user,password,unix_socket = unix_socket)
        else :
            mysqlHelper = MySQLHelper.MySQLHelper(host,user,password)
        return mysqlHelper