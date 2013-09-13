# -*- coding: utf-8 -*-
import urllib 
import urllib2 
import time
  
  
""" 
This is the "ystockquote" module. 
 
This module provides a Python API for retrieving stock data from Yahoo Finance. 
 
sample usage: 
>>> import ystockquote 
>>> print ystockquote.get_price('GOOG') 
529.46 
"""  
class StockHelper():
    def __init__(self, proxy='' ):
        self.proxy = proxy

    def set_proxy(self, proxy):
        self.proxy = proxy
 
    def __request(self, stock_id, stat):  
        symbol = self.__format_to_yahoo_symbol_from_num(stock_id)
        url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
        return self.__get(url).read().strip().strip('"')  

    def __format_to_yahoo_symbol_from_num(self, stock_id):
        stock_id = int(str(stock_id))
        stock_id = '%04d'%stock_id
        return stock_id + '.HK'

    def __format_to_sina_symbol_from_num(self, stock_id):
        stock_id = int(str(stock_id))
        stock_id = '%05d'%stock_id
        return 'hk' + stock_id


    def __get(self, url):
        if self.proxy != '':
            return   urllib.urlopen(url, proxies=self.proxy)  
        return urllib.urlopen(url)

        # proxy_support = urllib2.ProxyHandler(self.proxy)
        # opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        # urllib2.install_opener(opener)

        # return urllib2.urlopen(url)

    def get_chinese_name(self, stock_id):
        url = 'http://hq.sinajs.cn/list=' + self.__format_to_sina_symbol_from_num(stock_id)
        info = self.__get(url).read().strip().strip('"') .split(',')
        if len(info) > 1:
            return info[1]
        else :
            return ''
      
    def get_all(self, stock_id):  
        """ 
        Get all available quote data for the given ticker stock_id. 
         
        Returns a dictionary. 
        """  
        values = self.__request(stock_id, 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7').split(',')
        data = {}  
        data['price'] = values[0]  
        data['change'] = values[1]  
        data['volume'] = values[2]  
        data['avg_daily_volume'] = values[3]  
        data['stock_exchange'] = values[4]  
        data['market_cap'] = values[5]  
        data['book_value'] = values[6]  
        data['ebitda'] = values[7]  
        data['dividend_per_share'] = values[8]  
        data['dividend_yield'] = values[9]  
        data['earnings_per_share'] = values[10]  
        data['52_week_high'] = values[11]  
        data['52_week_low'] = values[12]  
        data['50day_moving_avg'] = values[13]  
        data['200day_moving_avg'] = values[14]  
        data['price_earnings_ratio'] = values[15]  
        data['price_earnings_growth_ratio'] = values[16]  
        data['price_sales_ratio'] = values[17]  
        data['price_book_ratio'] = values[18]  
        data['short_ratio'] = values[19]  
        return data  
          
          
    def get_price(self, stock_id):   
        return self.__request(stock_id, 'l1')  
      
      
    def get_change(self, stock_id):  
        return self.__request(stock_id, 'c1')  
          
          
    def get_volume(self, stock_id):   
        return self.__request(stock_id, 'v')  
      
      
    def get_avg_daily_volume(self, stock_id):   
        return self.__request(stock_id, 'a2')  
          
          
    def get_stock_exchange(self, stock_id):   
        return self.__request(stock_id, 'x')  
          
          
    def get_market_cap(self, stock_id):  
        return self.__request(stock_id, 'j1')  
         
         
    def get_book_value(self, stock_id):  
        return self.__request(stock_id, 'b4')  
      
      
    def get_ebitda(self, stock_id):   
        return self.__request(stock_id, 'j4')  
          
          
    def get_dividend_per_share(self, stock_id):  
        return self.__request(stock_id, 'd')  
      
      
    def get_dividend_yield(self, stock_id):   
        return self.__request(stock_id, 'y')  
          
          
    def get_earnings_per_share(self, stock_id):   
        return self.__request(stock_id, 'e')  
      
      
    def get_52_week_high(self, stock_id):   
        return self.__request(stock_id, 'k')  
          
          
    def get_52_week_low(sself, stock_id):   
        return self.__request(stock_id, 'j')  
      
      
    def get_50day_moving_avg(self, stock_id):   
        return self.__request(stock_id, 'm3')  
          
          
    def get_200day_moving_avg(self, stock_id):   
        return self.__request(stock_id, 'm4')  
          
          
    def get_price_earnings_ratio(self, stock_id):   
        return self.__request(stock_id, 'r')  
      
      
    def get_price_earnings_growth_ratio(self, stock_id):   
        return self.__request(stock_id, 'r5')  
      
      
    def get_price_sales_ratio(self, stock_id):   
        return self.__request(stock_id, 'p5')  
          
          
    def get_price_book_ratio(self, stock_id):   
        return self.__request(stock_id, 'p6')  
             
             
    def get_short_ratio(self, stock_id):   
        return self.__request(stock_id, 's7')  

    def get_name(self, stock_id):   
        return self.__request(stock_id, 'n')  
          
          
    def get_historical_prices(self, stock_id, start_date, end_date):  
        """ 
        Get historical prices for the given ticker stock_id. 
        Date format is 'YYYYMMDD' 
         
        Returns a nested list. 
        """  
        symbol = self.__format_to_yahoo_symbol_from_num(stock_id)
        url = 'http://ichart.yahoo.com/table.csv?s=%s&' % symbol + \
              'd=%s&' % str(int(end_date[4:6]) - 1) + \
              'e=%s&' % str(int(end_date[6:8])) + \
              'f=%s&' % str(int(end_date[0:4])) + \
              'g=d&' + \
              'a=%s&' % str(int(start_date[4:6]) - 1) + \
              'b=%s&' % str(int(start_date[6:8])) + \
              'c=%s&' % str(int(start_date[0:4])) + \
              'ignore=.csv'  
        days = self.__get(url).readlines()  
        data = [day[:-2].split(',') for day in days]  
        return data  


def main():
    stock_helper = StockHelper()
    # stock_helper.set_proxy({'http': 'http://web-proxy.oa.com:8080'})
    # print stock_helper.get_historical_prices('3888','20130601','20130626')
    print stock_helper.get_all('700')

    


if __name__ == '__main__':
	main()