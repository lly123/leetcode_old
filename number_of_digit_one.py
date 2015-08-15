__author__ = 'richard'


class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        def split(num):
            if num == 0:
                return [0], 1
            r = []
            length = 0
            while num > 0:
                r.insert(0, num % 10)
                num //= 10
                length += 1
            return r, length

        def merge(arr):
            return reduce(lambda s, v: s * 10 + v, arr, 0)

        def calculate(num, length):
            if length == 0:
                return 0
            else:
                digit = num[0]
                rest = num[1:]
                if digit == 0:
                    return calculate(rest, length - 1)
                elif digit == 1:
                    return calculate(*split(10 ** (length - 1) - 1)) + calculate(rest, length - 1) + merge(rest) + 1
                elif digit > 1:
                    return 10 ** (length - 1) + digit * calculate(*split(10 ** (length - 1) - 1)) + calculate(rest, length - 1)

        return calculate(*split(n))

print(Solution().countDigitOne(13))