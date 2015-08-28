__author__ = 'rli'

import sys


def look_and_say(length=sys.maxint):
    seq = '1'
    for _ in xrange(length):
        def read_and_remember(s, v):
            if s[-1][0] == v:
                s[-1] = (s[-1][0], s[-1][1] + 1)
            else:
                s.append((v, 1))
            return s
        yield seq
        d = reduce(read_and_remember, seq, [('', 0)])
        seq = ''.join([str(times) + num for (num, times) in d[1:]])


print([x for x in look_and_say(8)])


