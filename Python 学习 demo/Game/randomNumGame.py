# !/usr/bin/python3

'''
-*- coding: utf-8 -*-
@Author  : 博爱1616
@Time    : 2017/11/3 上午9:21
@Software: PyCharm
@File    : randomNumGame.py
'''

# 随机数模块
import random

# 生成1-100的一个随机数
random_num = random.randint(1, 101)

# while的意思就是，让它一直为真，也就是死循环，下面通过break来停止循环
while 1:

    input_num = int(input('请输入一个 1-100 的数字：'))

    # 判断输入的数字是否在1-100之间
    if input_num > 100 or input_num < 1:
        print('输入错误，请输入一个 1-100 的数字！')
        continue
    else:
        # 如果猜对了，结束循环
        if input_num == random_num:
            print('恭喜你，输入正确，结果为：', random_num)
            break
        # 如果猜小了，就跳出本次循环，提示猜小了
        elif input_num < random_num:
            print('输入的数字较小，请重新输入！')
            continue
        # 就三种情况，大、小等于，前面两种是等于和小于，那么 else 就是大于了，如果猜大了，就跳出本次循环，提示猜大了
        else:
            print('输入的数字较大，请重新输入！')
            continue

