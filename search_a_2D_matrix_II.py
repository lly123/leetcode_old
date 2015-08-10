__author__ = 'richard'


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        def binary_search(v, a, low, high):
            if high < low:
                return None, low - 1, low
            elif low > high:
                return None, high, high + 1
            else:
                middle = (high - low + 1) // 2 + low
                if a[middle] == v:
                    return middle, None, None
                elif a[middle] < v:
                    return binary_search(v, a, middle + 1, high)
                else:
                    return binary_search(v, a, low, middle - 1)

        def cut(m, vrl, vrh, hrl, hrh):
            return map(lambda r: r[hrl:hrh], m[vrl:vrh])

        def flat(m):
            return reduce(list.__add__, m)

        def search(v, m, width, height):
            if width == 0 or height == 0:
                return False
            elif height == 1:
                return binary_search(v, m[0], 0, width - 1)[0] is not None
            elif width == 1:
                return binary_search(v, flat(m), 0, height - 1)[0] is not None
            else:
                top_line = m[0]
                bottom_line = m[height - 1]
                left_line = flat(cut(m, 0, height, 0, 1))
                right_line = flat(cut(m, 0, height, width - 1, width))
                t_idx, tl, th = binary_search(v, top_line, 0, width - 1)
                b_idx, bl, bh = binary_search(v, bottom_line, 0, width - 1)
                l_idx, ll, lh = binary_search(v, left_line, 0, height - 1)
                r_idx, rl, rh = binary_search(v, right_line, 0, height - 1)
                if t_idx is not None or b_idx is not None or l_idx is not None or r_idx is not None:
                    return True
                else:
                    nm = cut(m, rl + 1, lh, bl + 1, th)
                    nm_width = th - (bl + 1)
                    nm_height = lh - (rl + 1)

                    width_middle = nm_width // 2
                    height_middle = nm_height // 2
                    m1_ret = search(v, cut(nm, 0, height_middle, 0, width_middle),
                                    width_middle, height_middle)
                    m2_ret = search(v, cut(nm, 0, height_middle, width_middle, nm_width),
                                    nm_width - width_middle, height_middle)
                    m3_ret = search(v, cut(nm, height_middle, nm_height, 0, width_middle),
                                    width_middle, nm_height - height_middle)
                    m4_ret = search(v, cut(nm, height_middle, nm_height, width_middle, nm_width),
                                    nm_width - width_middle, nm_height - height_middle)
                    return m1_ret or m2_ret or m3_ret or m4_ret

        return search(target, matrix, len(matrix[0]), len(matrix))

