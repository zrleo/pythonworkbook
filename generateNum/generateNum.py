# -*- coding:utf-8 -*-
import uuid
"""
生成200个随机字符串
"""
file = open("code.text",'w')
uuids = []
for i in range(200):
    i = i+1
    code = str(uuid.uuid1())
    s = str(code)

    print code
    print s
    file.write(code+'\n')

#file.write(code)

