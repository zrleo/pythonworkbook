# -*- coding:utf-8 -*-
import redis
import uuid

class Redis():

    def generateNum(self):
        '''
        生成促销码并保存在code.txt文件中
        '''
        file = open('code.txt', 'w')
        for i in range(200):
            code = uuid.uuid1()
            s = str(code)
            file.write(s + '\n')
    def redis(self):
        '''

        将生成的code存放进redis中
        '''
        r = redis.Redis(host='localhost',port=6379)
        with open('code.txt','r') as f:
            codes = f.readlines()
            for code in codes:

                r.set('code',code)
                print (r.get('code'))


if __name__ == '__main__':
    Redis().generateNum()
    Redis().redis()