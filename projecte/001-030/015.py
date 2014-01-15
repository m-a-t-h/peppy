#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Lattice Paths
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2015
"""

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../../module/' ))
from lattice import Lattice

def main():
    l = Lattice(20,20)
    answer = l.count_lattice_paths()
    sys.stdout.write("%s\n" %answer)

if __name__ == '__main__':
    main()

# 137846528820
