#!/usr/bin/python
#-*- coding:UTF-8 -*-
#########################################################################
# File Name: t.py
# Author: Junyi Li
# Personal page: dukeenglish.github.io
# Created Time: 23:32:45 2020-02-24
#########################################################################
import sys
f = open('tt.md')
fi = f.readlines()
for line in fi:
    if not line.strip():
        continue
    if '#' in line:
        print(line)
    elif 'ID' and '论文地址' not in line and '--------' not in line:
        line = line.strip().split('|')
        line[6] = '<font size=2>' + line[6] + '</font>'
        print('|'.join(line))
    else:
        print(line, end='')
    
