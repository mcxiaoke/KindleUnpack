#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-12-22 23:38:39
from __future__ import print_function, unicode_literals
import os,sys, shutil, re, codecs
'''
规范文件名工具

1. 所有的#&%.-_变为空格
2. 多个空格变为一个
3. 去掉所有的[] <> 【】《》 ()
4. 单词首字母大写
5. 扩展名不变
'''

CHARS = '#&%.-_<>[]［］【】《》（）\'"“”'

def fix_name(name):
    for c in CHARS:
        name = name.replace(c,' ')
    name = name.replace('文字版','').replace('azw3','')
    return name.replace('  ',' ').replace('  ',' ').strip()

def process(infile, debug=False):
    if debug:
        print('debug mode, only print ,no file renamed.')
    src = os.path.abspath(infile)
    fdir = os.path.dirname(src)
    sname = os.path.basename(src)
    name, ext = os.path.splitext(sname)
    dname = fix_name(name) + ext.lower()
    # output = os.path.join(fdir,'output')
    dst = os.path.join(fdir, dname)
    if dname == sname or os.path.exists(dst):
        print('Ignore exists:',sname)
        return
    print('SRC:',src)
    print('DST:',dst)
    if not debug:
        shutil.move(src, dst)
    # shutil.copy2(src, dst)

if __name__ == '__main__':
    path = os.path.abspath(unicode(sys.argv[1]))
    debug =(len(sys.argv) == 3 and sys.argv[2] == '-d')
    for n in os.listdir(path):
        process(os.path.join(path,n), debug=debug)
