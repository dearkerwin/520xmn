# -*- coding: utf-8 -*-
import sys   
sys.path.append("..")   
import INDEX
import StockHelper


stock_helper = StockHelper.StockHelper()
# stock_helper.set_proxy({'http': 'http://web-proxy.oa.com:8080'})
# print stock_helper.get_historical_prices('3888','20130601','20130626')
print stock_helper.get_all('700')