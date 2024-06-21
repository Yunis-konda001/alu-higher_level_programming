#!/usr/bin/env python3

def uppercase(s):
    uppercase_str = ""
    for c in s:
        uppercase_char = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        uppercase_str += uppercase_char
    print(uppercase_str)
