#!/usr/bin/env python
# http://codility.com/demo/results/demoAVPM9H-FYB/

def equi(A):
    # Temp counter to store sum of left part and right part accordingly
    left = 0
    right = sum(A)
    for i in xrange(len(A)):
        right -= A[i]
        if left == right:
            return i
        else:
            left += A[i]
    return -1

if __name__ == '__main__':
    print equi([-7, 1, 5, 2, -4, 3, 0])
    print equi([-1, 0, 1, -1, 0, 1, 6])
    print equi([0])
    print equi([])
