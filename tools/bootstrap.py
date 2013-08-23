# -*- coding: utf-8 -*-
''' 
  定义一些全局的函数
'''
import sys
import os

''' 向index插件差距， 把插件的lib 和 core 文件夹加载到系统路径'''
def register(plugin):
	path =  os.path.dirname(os.path.abspath(__file__))
	if not  path + "/" + plugin + "/lib" in sys.path:
	    sys.path.append( path +"/" + plugin + "/lib" )
	if not path + "/" + plugin + "/core" in sys.path:
	    sys.path.append( path + "/" + plugin + "/core")
