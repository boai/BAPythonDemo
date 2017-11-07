# !/usr/bin/python3

'''
-*- coding: utf-8 -*-
@Author  : 博爱1616
@Time    : 2017/11/3 上午10:57
@Software: PyCharm
@File    : zhuabao1.py
'''


import pypcappy
import dpkt
import time
import math
import os

import pcap

sniffer = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)
addr = lambda pkt, offset: '.'.join(str(ord(pkt[i])) for i in range(offset, offset + 4))
# for ts, pkt in sniffer:
# print('%d\tSRC %-16s\tDST %-16s' % (ts, addr(pkt, sniffer.dloff + 12), addr(pkt, sniffer.dloff + 16)))

print('test pcap!')




























































