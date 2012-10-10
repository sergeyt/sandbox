class WithTest(object):

    def __init__(self):
        self.greeting = 'hello'

    def __enter__(self):
        print 'greeting from __enter__()', self.greeting
        return self

    def __exit__(self, type, value, tb):
        print 'greeting from __exit__()', self.greeting
        print 'caught exception:\ntype=%s\nvalue=%s\ntb=%s' % (type, value, tb)

if __name__ == '__main__':
    with WithTest() as cm:
        print 'in main'
        print 'cm has greeting', cm.greeting
        print 1/0

