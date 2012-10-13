import sys
import inspect

def insertion_sort(seq):
    """Insert an item to a sorted seq"""
    print __whoami(), seq
    for i in xrange(1, len(seq)):
        j = i
        while j > 0 and seq[j] < seq[j-1]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        print seq

def selection_sort(seq):
    """Select the minimum one and replace the current positioned one"""
    print __whoami(), seq
    for i in xrange(0, len(seq)):
        min = i
        for j in xrange(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        seq[i], seq[min] = seq[min], seq[i]
        print seq

def bubble_sort(seq):
    """Swap neighbored number if not in order"""
    print __whoami(), seq
    for i in xrange(0, len(seq)):
        # Each round the min number will be put in the right place
        swapped = False
        for j in xrange(len(seq)-1, i, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
                swapped = True
        print seq
        if not swapped:
            break

def merge_sort(seq, p=0, r=-1):
    """Merge two sorted seq to one new sorted seq"""
    print __whoami(), seq
    if r == -1:
        r = len(seq) - 1
    if p < r:
        q = (p + r) / 2
        merge_sort(seq, p, q)
        merge_sort(seq, q+1, r)
        __merge_sort_merge_seq(seq, p, q, r)

def __merge_sort_merge_seq(seq, p, q, r):
    """Merge sorted sequence [p .. q] and [q+1 .. r] into new sorted seq,
    where p <= q < r.  Requires extra space 'left' and 'right'
    """
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

def quick_sort(seq, start=0, end=-1):
    """Partition the seq into [left-seq], seperator and [right-seq] where all
    items in left-seq are <= seperator and all items in right-seq are >
    seperator, then quick_sort left-seq and right-seq recursively
    """
    if end == -1:
        end = len(seq) - 1
    print __whoami(), seq, '(%d..%d)' % (start, end)
    if start < end:
        seperator = __quick_sort_partition(seq, start, end)
        print 'seperator: [%d] = %d' % (seperator, seq[seperator])
        print 'parted:', seq
        quick_sort(seq, start, seperator-1)
        quick_sort(seq, seperator+1, end)
    print seq

def __quick_sort_partition(seq, start, end):
    """Partition input seq and return the position of seperator, partition use
    the last element as pivot, use 'left' to record the rightmost position of
    element <= pivot, and use 'right' to record the to-compare element that >
    pivot.  Each round the algorithm partition it two 4 parts:

        (left-set)  {right-set}  untouched  [pivot]

    For example sequence:
        4 2 31 5 2 24 21 8
    => () {} 4 2 31 5 2 24 21 [8]   # initial state
    => (4) {} 2 31 5 2 24 21 [8]    # move left on if left <= pivot
    => (4 2) {31} 5 2 24 21 [8]     # ditto
    => (4 2 5) {31} 2 24 21 [8]     # swap left+1 and right when right <= pivot
    => (4 2 5 2) {31} 24 21 [8]     # ditto
    => (4 2 5 2) {31 24} 21 [8]     # otherwise move right on
    => (4 2 5 2) {31 24 21} [8]     # ditto
    => (4 2 5 2) [8] {24 21 31}     # swap left+1 and pivot
    => return left+1
    """
    left = start - 1
    for right in xrange(start, end):
        if seq[right] <= seq[end]:
            seq[left+1], seq[right] = seq[right], seq[left+1]
            left += 1
    seq[left+1], seq[end] = seq[end], seq[left+1]
    return left + 1

def __whoami():
    return inspect.stack()[1][3]

if __name__ == '__main__':
    seq = [4, 2, 31, 5, 2, 24, 21, 8]
    insertion_sort(seq[:])
    selection_sort(seq[:])
    bubble_sort(seq[:])
    merge_sort(seq[:])
    quick_sort(seq[:])

# vim:set tw=80 cc=+1 et sts=4 sw=4:
