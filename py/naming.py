#!/usr/bin/env python

class NamingTest:

    def __private(self): pass

    def _protected(self): pass

__private = 2
_protected = 3
public = 4
public2 = 5

__all__ = [ 'public' ]
