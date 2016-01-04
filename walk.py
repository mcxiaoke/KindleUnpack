#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-12-23 21:46:01
from __future__ import print_function, unicode_literals
import os
import sys

dirs = []
for dr, subdirs, names in os.walk('.'):
    for sd in subdirs:
        if sd.startswith('.'):
            subdirs.remove(sd)
        else:
            dirs.append(os.path.join(dr, sd))
for d in dirs:
    print(d)
