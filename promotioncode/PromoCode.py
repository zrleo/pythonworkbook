#-*- coding:utf-8 -*-

import uuid
import MySQLdb
from DBUtils.PooledDB import PooledDB

class PromoCode():
    def generateNum(self):
        '''
        生成促销码并保存在code.txt文件中

        '''
        file = open('code.text','w')
        for i in range(200):
            code = uuid.uuid1()
            s = str(code)
            file.write(s + '\n')

    def insertIntoMySQL(self):
        '''
        将生成的码插进mysql数据库
        '''
        pool = PooledDB(MySQLdb,10,host = 'localhost',user = 'root',
                passwd = '123456',db = 'coder',port = 3306)
        conn = pool.connection()
        cur = conn.cursor()
        sqlStatement = 'CREATE TABLE if NOT EXISTS MyCode (code CHAR (100) NOT NULL)'
        cur.execute(sqlStatement)

        with open('code.text','r') as f:
            codes = f.readlines()
            for code in codes:
                sql = "insert into MyCode values ('%s')"%str(code)
                cur.execute(sql)

        cur.close()
        conn.commit()
        conn.close()

if __name__ == '__main__':
    PromoCode().generateNum()
    PromoCode().insertIntoMySQL()
