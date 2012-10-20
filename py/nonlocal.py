#!/usr/bin/env python

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

if __name__ == '__main__':
    print make_counter()
    print make_counter()
    print make_counter()

# EOF
