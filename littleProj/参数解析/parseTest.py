#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/6/23
# @file parseTest.py
import argparse
import sys


def getOptions(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i", "--input", help="Your input file.")
    parser.add_argument("-o", "--output", help="Your destination output file.")
    parser.add_argument("-n", "--number", type=int, help="A number.")
    parser.add_argument("-v", "--verbose", dest='verbose', action='store_true', help="Verbose mode.")
    _options = parser.parse_args(args)
    return _options


options = getOptions(sys.argv[1:])
if options.verbose:
    print("Verbose mode on")
else:
    print("Verbose mode off")
print(options.input)
print(options.output)
print(options.number)
