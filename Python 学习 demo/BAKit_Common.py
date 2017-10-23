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
一些公共工具类
'''

import time, calendar
import os

# 格式当前日期时间，例如：2017-10-19 14:24:41
def ba_getCurrentTimeWithYMDHMS():
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print('获取系统当前日期时间：%s'%currentTime)
    return currentTime

# currentTime = ba_getCurrentTimeWithYMDHMS()
# print(currentTime)

# 获取指定年月的日历
def ba_getCurrentCalendarWithMonth(year, month):
    currentCalendar = calendar.month(year, month)
    print('获取系统%s年%s月的日历：\n%s \n'%(year, month, currentCalendar))
    return currentCalendar

# currentCalendar = ba_getCurrentCalendarWithMonth(2017, 10)
# print(currentCalendar)

# 简单算法：两个数-加法
def ba_algorithm_sum(num1, num2):
    a = num1 + num2
    print('%s + %s = %s'%(num1, num2, a))
    return a;





