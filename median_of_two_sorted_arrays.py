__author__ = 'richard'


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        def median(a1, a1_len, a2=None, a2_len=0):
            if a2 is None:
                if a1_len % 2 == 0:
                    return (a1[a1_len // 2 - 1] + a1[a1_len // 2]) / 2.0
                else:
                    return a1[a1_len // 2]
            elif a1_len == 1:
                if a2_len == 1:
                    return median([a1[0], a2[0]], 2)
                elif a2_len % 2 == 0:
                    return median(sorted([a1[0], a2[a2_len // 2 - 1], a2[a2_len // 2]]), 3)
                else:
                    return median(sorted([a1[0], a2[a2_len // 2 - 1], a2[a2_len // 2], a2[a2_len // 2 + 1]]), 4)
            elif a1_len == 2:
                if a2_len == 2:
                    return median(sorted([a1[0], a1[1], a2[0], a2[1]]), 4)
                elif a2_len % 2 == 0:
                    return median(sorted([a1[0], a1[1], a2[a2_len // 2 - 2], a2[a2_len // 2 - 1],
                                          a2[a2_len // 2], a2[a2_len // 2 + 1]]), 6)
                else:
                    return median(sorted([a1[0], a1[1], a2[a2_len // 2 - 1], a2[a2_len // 2], a2[a2_len // 2 + 1]]), 5)
            elif a1[a1_len // 2] > a2[a2_len // 2]:
                a1 = a1[:a1_len // 2 + 1]
                a2 = a2[a1_len - (a1_len // 2 + 1):]
                return median(a1, a1_len // 2 + 1, a2, a2_len - (a1_len - (a1_len // 2 + 1)))
            else:
                middle = a1_len // 2 - 1 if a1_len % 2 == 0 else a1_len // 2
                a1 = a1[middle:]
                a2 = a2[:a2_len - middle]
                return median(a1, a1_len - middle, a2, a2_len - middle)

        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == len2 == 0:
            return []
        elif len1 == 0:
            return median(nums2, len2)
        elif len2 == 0:
            return median(nums1, len1)
        elif len1 <= len2:
            return median(nums1, len1, nums2, len2)
        else:
            return median(nums2, len2, nums1, len1)
