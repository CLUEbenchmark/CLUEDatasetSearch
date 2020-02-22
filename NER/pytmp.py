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
    tt = tmp[0]+tmp[2:]
    k.append(tt)
    tmp = f.readline()
    tt = tmp[0]+tmp[2:]
    k.append(tt)
    line = f.readlines()
# print(k, tmp)
for i in line:
    i = i.strip().split('|')
    firstc = '['+i[1].strip()+']'+'('+i[2].strip()+')' 
    output = [firstc]
    output += i[3:]
    k.append(output)
print(k[0])
print(k[1])
for i in k[2:]:
    print('|'+'|'.join(i))
