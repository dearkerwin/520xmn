import sys; 
if not "./lib" in sys.path:
    sys.path.append("./lib") 

import MySQLHelper

mysql =MySQLHelper.MySQLHelper('localhost','root','123456')
# /tmp/mysql.sock
mysql.selectDb('520xmn')
insert_data = {
	'src' : 'testseerc2e',
	'path' : 'path',
	'file_name' : 'one.jpg'
}
mysql.insert('pic',insert_data)
ret = mysql.queryAll("select count(*) from pic where 1")
print ret