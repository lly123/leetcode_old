__author__ = 'richard'

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
# not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        def find_kth_largest(arr, k):
            def split(s, v):
                s[0].append(v) if v > arr[0] else s[1].append(v)
                return s
            r = reduce(split, arr[1:], ([], []))
            left_len = len(r[0])
            if left_len == k - 1:
                return arr[0]
            elif left_len >= k:
                return find_kth_largest(r[0], k)
            else:
                return find_kth_largest(r[1], k - left_len - 1)
        return find_kth_largest(nums, k)

print(Solution().findKthLargest([1, 2, 9, 1, 3, 8, 7, 5, 1], 2))
