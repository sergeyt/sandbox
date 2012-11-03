#!/usr/bin/env python
# http://codility.com/demo/results/demoVRPKX7-TSH/

def equi(A):
    # Temp array to store sum value for each index, where position i stores sum
    # of A[0..i-1], like this:
    #
    # [0, sum for [0], sum for [1], ..., sum for [n-1], 0]
    #
    sum_index = [0]
    for i in xrange(len(A)):
        sum_index.append(sum_index[i] + A[i])
    sum_index.append(0)

    for i in xrange(0, len(A)):
        if sum_index[i] == sum_index[-2] - A[i] - sum_index[i]:
            return i
    return -1

if __name__ == '__main__':
    print equi([-7, 1, 5, 2, -4, 3, 0])
    print equi([-1, 0, 1, -1, 0, 1])
    print equi([0])
