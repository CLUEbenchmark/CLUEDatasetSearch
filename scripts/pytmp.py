#!/usr/bin/python
#-*- coding:UTF-8 -*-
#########################################################################
# File Name: pytmp.py
# Author: Junyi Li
# Personal page: dukeenglish.github.io
# Created Time: 21:59:43 2020-02-22
#########################################################################
import sys
file = sys.argv[1]
k = []
with open(file) as f:
    tmp = f.readline()
    tmp = f.readline()
    line = f.readlines()
# print(k, tmp)
for i in line:
    i = i.strip().split('|')
    firstc = '['+i[1].strip()+']'+'('+i[2].strip()+')' 
    output = [firstc]
    output += i[3:]
    k.append(output)
print('|ID|标题  | 数据集更新日期 | 数据集提供者                           | 许可 | 说明                                                         | 关键字       | 类别         | 论文地址                                      | 备注 |')
print('|---|------------------------------------ | -------------- | -------------------------------------- | ---- | ------------------------------------------------------------ | ------------ | ------------ | --------------------------------------------- | ---- |')
for n, i in enumerate(k):
    print('|'+str(n+1)+'|'+'|'.join(i))
