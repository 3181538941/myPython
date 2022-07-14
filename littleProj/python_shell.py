#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/10
# @file python_shell.py
def python_shell():
    while True:
        try:
            pycmd = input(">>> ")
            if pycmd in globals().keys():
                print(globals()[pycmd])
                continue
            elif pycmd == 'about':
                print("BINPython By:XINGYUJIE[https://github.com/xingyujie] AGPL-3.0 LICENSE Release")
            elif pycmd == 'help':
                print("Type help() for interactive help, or help(object) for help about object.")
            elif pycmd == 'license':
                print("Type license() to see the full license text")
            else:
                exec(pycmd)
        except KeyboardInterrupt:
            print("EXIT!")
            sys.exit()
        except Exception as err:
            print(err)


if __name__ == '__main__':
    python_shell()
