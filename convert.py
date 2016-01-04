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


def delete(afile):
    try:
        os.remove(afile)
    except OSError, e:
        pass


def cleanup(outdir):
    shutil.rmtree(os.path.join(outdir, 'mobi8'), ignore_errors=True)
    shutil.rmtree(os.path.join(outdir, 'mobi7'), ignore_errors=True)
    shutil.rmtree(os.path.join(outdir, 'Images'), ignore_errors=True)
    shutil.rmtree(os.path.join(outdir, 'HDImages'), ignore_errors=True)
    delete(os.path.join(outdir, 'kindlegensrc.zip'))


def unpack(indir, outdir):
    outdir = outdir or indir
    print('Input Path: %s' % indir)
    print('Output Path: %s' % outdir)
    files = [os.path.join(indir, f) for f in unipath.listdir(indir) if f.endswith('.azw3') or f.endswith('.mobi')]
    if outdir and not unipath.exists(outdir):
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
            ok.write('%s\n' % f)
        except BaseException as e:
            print("Error: %s" % e)
            error.write('Error: unpack file: %s\n' % f)
            continue
    cleanup(outdir)
    ok.close()
    error.close()


def get_dirs(root):
    dirs = []
    for sd in subdirs:
        if sd.startswith('.'):
            subdirs.remove(sd)
        else:
            dirs.append(os.path.join(dr, sd))
    return dirs


def main(argv=unicode_argv()):
    if len(argv) < 2:
        print("Usage:", argv[0], "input_dir [output_dir]")
    indir = argv[1]
    outdir = argv[2] if len(argv) > 2 else None
    dirs = get_dirs(indir)
    for d in dirs:
        unpack(d, outdir)
    unpack(indir, outdir)
    return 0

if __name__ == "__main__":
    sys.exit(main())
