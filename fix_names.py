#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-12-22 23:38:39
from __future__ import print_function, unicode_literals
import os,sys, shutil, re, codecs, traceback, time, string

import lib.unipath as unipath
from lib.unipath import pathof

'''
规范文件名工具

1. 所有的#&%.-_变为空格
2. 多个空格变为一个
3. 去掉所有的[] <> 【】《》 ()
4. 单词首字母大写
5. 扩展名不变
'''

EXTENSIONS = ['.mobi', '.epub', '.azw3', '.pdf']
CHARS = '#&%._<>[]［］【】《》（）\'"“”'
STRIP_NUM_PREFIX = r'\d+\s(.*)'

def fix_name(name):
    for c in CHARS:
        name = name.replace(c,' ')
    name = name.replace('文字版','').replace('azw3','')
    name =  name.replace('  ',' ').replace('  ',' ').strip()
    name =  string.capwords(name)
    m = re.compile(STRIP_NUM_PREFIX).match(name)
    return m.group(1) if m else name

def process(infile, debug=False):
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
    # print('SRC:',src)
    if not debug:
        print('DST:',dst)
        shutil.move(src, dst)
        return dst
    # shutil.copy2(src, dst)

if __name__ == '__main__':
    path = unipath.abspath(sys.argv[1])
    debug =(len(sys.argv) == 3 and sys.argv[2] == '-d')
    if debug:
        print('DEBUG MODE')
    files = []
    for dir, subdirs, names in os.walk(path):
        for name in names:
            files.append(os.path.join(dir,name))
    files = [f for f in files if os.path.splitext(os.path.basename(f))[1] in EXTENSIONS]
    log_name = 'error-%s.log' % time.strftime("%Y%m%d%H%M%S", time.localtime())
    error = codecs.open(log_name, 'w', encoding='utf8')
    #bad = unipath.abspath('bad')
    #if not unipath.exists(bad):
    #    os.mkdir(bad)
    for f in files:
        try:
            process(f, debug=debug)
        except BaseException as e:
            traceback.print_exc()
            #print("Error: %s" % e)
            error.write('File: [%s]\nError: [%s]\n\n' % (f, traceback.format_exc()))
            #shutil.copy(f, bad)
            continue
    error.close()
    print('Process finished for %s' % path)
