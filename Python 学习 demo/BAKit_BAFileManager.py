#!/usr/bin/env python
# encoding: utf-8

"""
@author: 博爱
@contact: QQ：137361770
@software: PyCharm
@file: BAKit_BAFileManager.py
@blog：http://boaihome.com
@time: 2017/10/20 0001 13:14
"""

'''
对文件操作的工具模块
'''

import os


# 1、将A文件复制到B文件中去(保持原来格式)
def ba_fileManager_copyFile (inputFile, outputFile, encoding):
    fin = open(inputFile, 'r', encoding=encoding) #以读的方式打开文件
    fout = open(outputFile, 'w', encoding=encoding) #以写得方式打开文件
    for eachLiine in fin.readlines(): #读取文件的每一行
        line = eachLiine.strip() #去除每行的首位空格
        fout.write(line + '\n')
    fin.close()
    fout.close()

# 2、读取文件中的内容,返回List列表 (加载本地词典库)
def ba_fileManager_readFile_list(inputFile, encoding):
    results = []
    fin = open(inputFile, 'r', encoding=encoding)
    for eachLiine in fin.readlines():
        line = eachLiine.strip().replace('\ufeff', '')
        results.append(line)
    fin.close()
    return results

# 3、读取文件，返回文件内容
def ba_fileManager_readFile(filePath):
    with open(filePath, 'r+', encoding = 'UTF-8') as f:
        str = f.read()
    return str.strip().replace('\ufeff', '')

# 4、改变文件名字，将原文件名字改变为新的名字
def ba_fileManager_rename(oldName, newName):
    os.rename(oldName, newName)
    return

# 5、删除文件
def ba_fileManager_removeFile(fileName):
    os.remove(fileName)
    return

# 6、新建文件夹
def ba_fileManager_mkdir(folderName):
    os.mkdir(folderName)
    return

# 7、获取当前文件的目录
def ba_fileManager_getcwd():
    path = os.getcwd()
    print('当前路径：', path)
    return path

# 8、进入指定目录
def ba_fileManager_chdir(newPath):
    path = os.chdir(newPath)
    return path

# 9、删除指定目录
def ba_fileManager_rmdir(newPath):
    path = os.rmdir(newPath)
    return path




def func():
    pass


# if __name__ == '__main__':
#     ba_fileManager_copyFile('test1.txt', 'text.txt','UTF-8')
#     contents = ba_fileManager_readFile_list('../dict/time.dict','UTF-8')
#     print(contents)
