__author__ = 'richard'


def cut(prices, length):
    m = [None] * (length + 1)
    m[0] = ([], 0)

    for i in xrange(1, length + 1):
        def calculate(s, v):
            s.append((m[i - v][0] + [v], m[i - v][1] + prices[v]))
            return s
        m[i] = max(reduce(calculate, xrange(1, i + 1), []), key=lambda v: v[1])

    return m[-1]


print(cut({1: 3, 2: 5, 3: 10, 4: 11, 5: 12}, 5))