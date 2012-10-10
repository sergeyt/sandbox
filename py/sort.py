import sys
import inspect

def insertion_sort(seq):
    '''insert an item to a sorted seq'''
    print __whoami(), seq
    for i in xrange(1, len(seq)):
        j = i
        while j > 0 and seq[j] < seq[j-1]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        print seq

def selection_sort(seq):
    '''select the minimum one and replace the current positioned one'''
    print __whoami(), seq
    for i in xrange(0, len(seq)):
        min = i
        for j in xrange(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        seq[i], seq[min] = seq[min], seq[i]
        print seq

def bubble_sort(seq):
    '''swap neighbored number if not in order'''
    print __whoami(), seq
    for i in xrange(0, len(seq)):
        swapped = False
        for j in xrange(len(seq)-1, i, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
                swapped = True
        print seq
        if not swapped:
            break

def merge_sort(seq, p=0, r=-1):
    '''merge to sorted seq to one new sorted seq'''
    print __whoami(), seq
    if r == -1:
        r = len(seq) - 1
    if p < r:
        q = (p + r) / 2
        merge_sort(seq, p, q)
        merge_sort(seq, q+1, r)
        __merge(seq, p, q, r)

def __merge(seq, p, q, r):
    '''merge sorted sequence [p .. q] and [q+1 .. r] into new sorted seq,
    where p <= q < r'''
    left = seq[p:q+1]
    left.append(sys.maxint)
    right = seq[q+1:r+1]
    right.append(sys.maxint)
    i = 0
    j = 0
    for k in xrange(p, r+1):
        if left[i] <= right[j]:
            seq[k] = left[i]
            i += 1
        else:
            seq[k] = right[j]
            j += 1
    print seq

def __whoami():
    return inspect.stack()[1][3]

if __name__ == '__main__':
    seq = [4, 2, 31, 5, 2, 24, 21, 8]
    insertion_sort(seq[:])
    selection_sort(seq[:])
    bubble_sort(seq[:])
    merge_sort(seq[:])

# vim:set tw=80 cc=+1 et sts=4 sw=4:
