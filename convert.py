#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-12-22 07:19:06
from __future__ import print_function

import sys

from lib.compatibility_utils import PY2, text_type, unicode_str
from lib.compatibility_utils import unicode_argv, add_cp65001_codec

import lib.unipath as unipath
from lib.unipath import pathof

import os
import traceback

import codecs
add_cp65001_codec()

import lib.kindleunpack as kindleunpack

def unpack(indir, outdir):
    print('Input Path = "'+ indir + '"\n')
    print('Output Path = "' + outdir + '"\n')
    files = [os.path.join(indir,f) for f in unipath.listdir(indir) if f.endswith('.azw3')]
    try:
        for f in files:
            print("Process azw3 file: %s" % f)
            kindleunpack.unpackBook(f, outdir)
    except Exception as e:
        print("Error: %s" % e)
        print(traceback.format_exc())

def main(argv=unicode_argv()):
    print("Command Line Arguments:", argv)
    unpack(argv[1], argv[2])
    return 0

if __name__ == "__main__":
    sys.exit(main())
