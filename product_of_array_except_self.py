__author__ = 'richard'

# Given an array of n integers where n > 1, nums, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        num_len = len(nums)

        def cal((r, b, l), v):
            r[v] *= b
            r[num_len - 1 - v] *= l
            b *= nums[v]
            l *= nums[num_len - 1 - v]
            return r, b, l

        return reduce(cal, range(num_len), ([1] * num_len, 1, 1))[0]

print(Solution().productExceptSelf([4, 5, 6]))