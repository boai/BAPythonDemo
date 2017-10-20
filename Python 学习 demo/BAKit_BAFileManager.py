#!/usr/bin/env python
# encoding: utf-8

"""
@author: 博爱
@contact: QQ：137361770
@software: PyCharm
@file: BAKit_BAFileManager.py
@time: 2017/10/20 0001 13:14
"""

'''
对文件操作的工具模块
'''


# 1.将A文件复制到B文件中去(保持原来格式)
def ba_fileManager_copyFile (inputFile, outputFile, encoding):
    fin = open(inputFile, 'r', encoding=encoding) #以读的方式打开文件
    fout = open(outputFile, 'w', encoding=encoding) #以写得方式打开文件
    for eachLiine in fin.readlines(): #读取文件的每一行
        line = eachLiine.strip() #去除每行的首位空格
        fout.write(line + '\n')
    fin.close()
    fout.close()

# 2. 读取文件中的内容,返回List列表 (加载本地词典库)
def ba_fileManager_readFile_list(inputFile, encoding):
    results = []
    fin = open(inputFile, 'r', encoding=encoding)
    for eachLiine in fin.readlines():
        line = eachLiine.strip().replace('\ufeff', '')
        results.append(line)
    fin.close()
    return results

# 3.读取文件，返回文件内容
def ba_fileManager_read(filePath):
    with open(filePath, 'r+', encoding = 'UTF-8') as f:
        str = f.read()
    return str.strip().replace('\ufeff', '')

def func():
    pass


# if __name__ == '__main__':
#     ba_fileManager_copyFile('../data/test1.txt', '../data/text.txt','UTF-8')
#     contents = ba_fileManager_readFile_list('../dict/time.dict','UTF-8')
#     print(contents)
