#!/usr/bin/env python

import sys,os
import shutil, errno

cwd = os.getcwd()
run = os.system

def copydir(src, dst):
    for src_dir, dirs, files in os.walk(src):
        dst_dir = src_dir.replace(src, dst, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)

publish_dir = os.path.join(cwd, "..", "xjump.github.io")
public_dir = os.path.join(cwd, "public")

run('zola build')

copydir(public_dir, publish_dir)

run('zola serve')