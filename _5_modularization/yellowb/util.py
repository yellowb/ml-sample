# -*- coding: utf-8 -*-

'Sample module for demo'

__author__ = 'yellowb'


def _calculate(x, y):
    return x + y


def calculate(x, y):
    print(__name__)  # will print different values in running this module directly and included as module by others.
    print('do calculation for %s + %s' % (x, y))
    return _calculate(x, y)


if __name__ == '__main__':
    # test
    calculate(1, 1)
