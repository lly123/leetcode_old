__author__ = 'rli'


def min_neighbor_right(arr):
    def fn(s, v):
        while len(s[0]) > 0:
            x = s[0].pop()
            if x > v[1]:
                s[1].append((x, v[1]))
            else:
                s[0].append(x)
                break
        return s[0] + [v[1]], s[1]
    return reduce(fn, enumerate(arr[1:]), ([arr[0]], []))

min_arr = min_neighbor_right([2, 30, 5, 8, 10, 2, 3, 6, 1])
print(min_arr)
