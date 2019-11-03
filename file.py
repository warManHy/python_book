# coding: utf-8
import os
import sys

def read_file(file):
    with open(file) as filename:
        contents = filename.read()
        return contents  #返回了文本的所有内容

def read_line(file):
    with open(file) as filename:
        for line in filename:
            print line  #按行输出文件每一行，会多个换行符
            print line.rstrip()  # 去除换行符 

def read_line1(file):
    with open(file) as filename:
        lines = filename.readlines()
    for line in lines:
        print line.rstrip()

def test_file(file):
    with open(file) as filename:
        lines = filename.readlines()
    p_str = ''
    for line in lines:
        p_str += line.rstrip()
    
    input_str = raw_input("please input string check : ")
    if input_str in p_str:
        print 'u input in file'
    else:
        print 'u not in'

def write(file):
    with open(file, 'w') as filename:  
        #w 写入模式，文件先清空 
        #r 默认只读模式
        #a 附加模式 不请客文件
        filename.write("hanyan")

# test_file('./dog.py')
write('test.tx')
         