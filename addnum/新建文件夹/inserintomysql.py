#-*- coding:utf-8 -*-
import MySQLdb
from DBUtils.PooledDB import PooledDB

pool = PooledDB(MySQLdb,10,host = 'localhost',user = 'root',
                passwd = '123456',db = 'coder',port = 3306)
conn = pool.connection()
cur = conn.cursor()
sqlStatement = 'CREATE TABLE if NOT EXISTS mykeys (key_id CHAR (36) NOT NULL)'
cur.execute(sqlStatement)

with open('code.text','r') as f:
    keys = f.readlines()
    for key in keys:
        cur.execute("insert into mycode values ('%s')"%str(key))

cur.close()
conn.commit()
conn.close()