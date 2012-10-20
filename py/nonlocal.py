#!/usr/bin/env python3

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

if __name__ == '__main__':
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())

# EOF
