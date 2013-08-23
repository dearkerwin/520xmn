# -*- coding: utf-8 -*-
import sys
import os
import bootstrap


''' 加载公共资源和配置 ''' 
bootstrap.register("common")

'''加载stock'''
bootstrap.register("stock")

'''加载getpic'''
bootstrap.register("getpic")

''' 定义全局变量'''
ROOT_PATH =  os.path.dirname(os.path.abspath(__file__))
from database import DBCONFIG 




    

