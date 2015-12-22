#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-12-22 07:19:06
from __future__ import print_function, unicode_literals

import sys
import shutil

from lib.compatibility_utils import PY2, text_type, unicode_str
from lib.compatibility_utils import unicode_argv, add_cp65001_codec

import lib.unipath as unipath
from lib.unipath import pathof

import os
import traceback

import codecs
add_cp65001_codec()

import lib.kindleunpack as kindleunpack

def cleanup(outdir):
    shutil.rmtree(os.path.join(outdir,'mobi8'), ignore_errors=True)
    shutil.rmtree(os.path.join(outdir,'mobi7'), ignore_errors=True)
    shutil.rmtree(os.path.join(outdir,'Images'), ignore_errors=True)
    shutil.rmtree(os.path.join(outdir,'HDImages'), ignore_errors=True)

def unpack(indir, outdir):
    print('Input Path = "'+ indir)
    print('Output Path = "' + outdir)
    files = [os.path.join(indir,f) for f in unipath.listdir(indir) if f.endswith('.azw3') or f.endswith('.mobi')]
    if not unipath.exists(outdir):
        unipath.mkdir(outdir)
    ok = codecs.open(os.path.join(outdir, 'ok.log'), 'w', encoding='utf8')
    error = codecs.open(os.path.join(outdir, 'error.log'), 'w', encoding='utf8')
    for f in files:
        try:
            print("Process Book file: %s" % f)
        except UnicodeEncodeError as e:
            # print("Process Book file:",f.decode('gbk'))
            pass
        try:
            cleanup(outdir)
            kindleunpack.unpackBook(f, outdir)
            ok.write('OK: unpack file: %s\n' % f)
        except BaseException as e:
            print("Error: %s" % e)
            error.write('Error: unpack file: %s\n' % f)
            continue
    cleanup(outdir)
    ok.close()
    error.close()

def main(argv=unicode_argv()):
    if len(argv) != 3:
        print("Usage:", argv[0], "input_dir output_dir")
        sys.exit(1)
    unpack(argv[1], argv[2])
    return 0

if __name__ == "__main__":
    sys.exit(main())
