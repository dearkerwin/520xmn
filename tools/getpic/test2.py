import MySQLdb 

conn = MySQLdb.connect(host='localhost', user='root',passwd='123456')

cursor = conn.cursor()   


conn.select_db('520xmn');   

# cursor.execute("""create table test(id int, info varchar(100)) """)   

value = [1,"inserted ?"];   

cursor.execute("insert into test values(%s,%s)",value);   

values=[]   

for i in range(20):   
    values.append((i,'Hello mysqldb, I am recoder ' + str(i)))   


cursor.executemany("""insert into test values(%s,%s) """,values);   

cursor.close();  