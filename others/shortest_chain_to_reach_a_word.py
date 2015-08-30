__author__ = 'rli'

# Length of shortest chain to reach a target word

# Given a dictionary, and two words 'start' and 'target' (both of same length).
# Find length of the smallest chain from 'start' to 'target' if it exists,
# such that adjacent words in the chain only differ by one character and
# each word in the chain is a valid word i.e., it exists in the dictionary.
# It may be assumed that the 'target' word exists in dictionary and
# length of all dictionary words is same.


def shortest_chain(begin_word, target_word, dictionary):
    def foldm(fn, l):
        return reduce(list.__add__, [fn(x) for x in l])

    def chain_word(chain):
        def is_adjacent(w1, w2):
            if len(w1) == len(w2):
                pairs = zip(w1, w2)
                return reduce(lambda s, v: s + 1 if v[0] != v[1] else s, pairs, 0) == 1
            return False

        def each_with_rest(fn, l):
            for i in xrange(len(l)):
                fn(l[i], l[0:i] + l[i + 1:])

        def fn(w, ws):
            if is_adjacent(chain[0][-1], w):
                ret.append((chain[0] + [w], ws))

        ret = []
        each_with_rest(fn, chain[1])
        return ret

    chain_list = [([begin_word], dictionary)]
    while len(chain_list) > 0:
        chain_list = foldm(chain_word, chain_list)
        for c in chain_list:
            if c[0][-1] == target_word:
                return c[0]
    return None


print(shortest_chain('TOON', 'PLEA', ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']))

