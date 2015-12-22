#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-12-22 23:38:39
from __future__ import print_function, unicode_literals
import os,sys, shutil, codecs
'''
规范文件名工具

1. 所有的#&%.-_变为空格
2. 多个空格变为一个
3. 去掉所有的[] <> 【】《》 ()
4. 单词首字母大写
5. 扩展名不变
'''

def process(infile):
    path = os.path.abspath(infile)
    fdir = os.path.dirname(path)
    bname = os.path.basename(path)
    name, ext = os.path.splitext(bname)
    print(name,'+',ext)

if __name__ == '__main__':
    path = os.path.abspath(unicode(sys.argv[1]))
    for n in os.listdir(path):
        process(os.path.join(path,n))
