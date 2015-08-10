__author__ = 'richard'

from collections import defaultdict


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        def word2dict(w):
            def inc(d, a):
                d[a] += 1
                return d
            return reduce(inc, w, defaultdict(int))
        return word2dict(s) == word2dict(t)

