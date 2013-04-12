# -*- coding:utf-8 -*-
# Created on 2013-4-06
# @author: kerwin

import MySQLdb
class MySQLHelper:
    def __init__(self,host,user,password, db = '', unix_socket = '', charset="utf8", ):
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset
        try:
            if unix_socket != '':
                self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.password, unix_socket=unix_socket)
            else:
                self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.password)
            self.conn.set_character_set(self.charset)
            self.cur=self.conn.cursor()

            if db != '':
                self.selectDb(db)

        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


    def selectDb(self,db):
      try:
          self.conn.select_db(db)
      except MySQLdb.Error as e:
          print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self,sql):
        try:
           n=self.cur.execute(sql)
           print sql
           return n
        except MySQLdb.Error as e:
           print("Mysql Error:%s\nSQL:%s" %(e,sql))

    def queryRow(self,sql):
        self.query(sql)
        result = self.cur.fetchone()
        return result

    def queryAll(self,sql):
        self.query(sql)
        result=self.cur.fetchall()
        desc =self.cur.description
        d = []
        for inv in result:
             _d = {}
             for i in range(0,len(inv)):
                 _d[desc[i][0]] = str(inv[i])
             d.append(_d)
        return d

    def find(self, tablename, condition, fields= "*"):
        field = self._getFields(fields)
        condition = self._getConditions(condition)
        sql="select "+field+ " from "+ tablename+ " where "+ condition + " limit 1"
        ret = self.queryAll(sql)
        if len(ret) > 0:
            return ret[0]
        else:
            return ret

    def findAll(self, tablename, condition, fields = "*"): 
        field = self._getFields(fields)
        condition = self._getConditions(condition)
        sql="select "+field+ " from "+ tablename+ " where "+ condition
        ret = self.queryAll(sql)
        return ret

    def count(self, tablename, condition):
        condition = self._getConditions(condition)
        sql="select count(*) as count from "+ tablename+ " where "+ condition 
        ret = self.queryAll(sql)
        return ret

    def save(self,p_table_name,p_data):
        for key in p_data:
            p_data[key] = "'"+str(p_data[key])+"'"
        key   = ','.join(p_data.keys())
        value = ','.join(p_data.values())
        real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value + ")"
        #self.query("set names 'utf8'")
        ret = self.query(real_sql)
        self.commit()
        return ret

    def _getFields(self, fields):
        fieldString = ''
        if isinstance(fields, ( str )):
            fieldString = fields
        elif isinstance(fields, ( list )):
            fieldString = ','.join(fields) 

        if fieldString == '':
            fieldString = "*"
        return fieldString

    def _getConditions(self, conditions):
        cString = ''
        if isinstance(conditions, ( str )):
            cString = conditions
        elif isinstance(conditions, ( list,dict )):
            con = []
            for c in conditions:
                con.append("`" + str(c) + "` = '" + str(conditions[c]) + "'") 
            cString =' and '.join(con)

        if cString == '':
            cString = " 1 = 1"
        return cString

    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()