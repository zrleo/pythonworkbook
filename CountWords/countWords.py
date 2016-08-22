# -*- coding:utf-8 -*-
import re

def countWords():

    with open('word.txt','r') as f:
        data = f.read()

    words = re.compile(r'([a-zA-Z]+)')

    dic = {}
    for i in words.findall(data):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1

    list = []
    for k,value in dic.items():
        list.append((k,value))

    list.sort(key=lambda t:t[0])

    for i in list:
        print (i[0],i[1])





if __name__ == '__main__':
    countWords()