#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1.2 Write code to reverse a C-Style String (C-String means that “abcd” is
    represented as five characters, including the null character )
"""

def reverse_c_str(cstr):
    seq = list(cstr)
    head = 0
    tail = len(seq) - 1
    while head < tail:
        seq[head], seq[tail] = seq[tail], seq[head]
        head += 1
        tail -= 1
    return ''.join(seq)

if __name__ == '__main__':
    print reverse_c_str("abcdefg\0")
