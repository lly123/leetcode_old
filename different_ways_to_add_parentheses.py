__author__ = 'richard'


class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        import re

        plus = lambda x: lambda y: x + y
        minus = lambda x: lambda y: x - y
        times = lambda x: lambda y: x * y

        def compute(ops, nums):
            if len(nums) == 1:
                return [nums[0]]
            elif len(nums) == 2:
                return [ops[0](nums[0])(nums[1])]
            else:
                return [op(x)(y) for i, op in enumerate(ops)
                        for x in compute(ops[:i], nums[:i + 1])
                        for y in compute(ops[i + 1:], nums[i + 1:])]

        nums = map(lambda n: int(n), re.split('[\*\-\+]', input))
        ops = map(lambda op: plus if op == '+' else minus if op == '-' else times, re.split('[0-9]+', input)[1:-1])
        return compute(ops, nums)
