#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Demo bsearch a sorted sequence"""

def bsearch(seq, key):
    lo = 0
    hi = len(seq) - 1
    while lo < hi:
        print 'bsearch in [%d .. %d]' % (lo, hi)
        mid = (lo + hi) / 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid

if __name__ == '__main__':
    print bsearch((), 1)
    print bsearch(range(100), 101)
    print bsearch(range(100), 5)

# EOF
