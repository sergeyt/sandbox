#!/usr/bin/env python

"""
This only see the explicitly declared in __all__:

    >>> from visibility import *
    >>> dir()

"""

__all__ = [ 'public' ]

__global_private = 0
_global_protected = 0
global_public = 0
global_public2 = 0

class VisibilityTest:
    __private = 0
    _protected = 0

if __name__ == '__main__':
    # All global variables are visible
    print dir()

    v = VisibilityTest()
    # __private is not visible
    print dir(v)

# vim:set et sts=4 sw=4:
