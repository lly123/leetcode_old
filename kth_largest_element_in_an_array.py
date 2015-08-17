__author__ = 'richard'


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        class Heap:
            def __init__(self, arr, length):
                self.arr = arr
                self.length = length

            def sink(self, i):
                left = 2 * i + 1
                right = 2 * i + 2
                if left < self.length:
                    maximum = right if right < self.length and self.arr[right] > self.arr[left] else left
                    if self.arr[maximum] > self.arr[i]:
                        tmp = self.arr[i]
                        self.arr[i] = self.arr[maximum]
                        self.arr[maximum] = tmp
                        self.sink(maximum)

            def heapify(self):
                for i in xrange((self.length - 2) // 2, -1, -1):
                    self.sink(i)

            def extract_max(self):
                r = self.arr[0]
                self.arr[0] = self.arr[self.length - 1]
                self.arr[self.length - 1] = r
                self.length -= 1
                self.sink(0)
                return r

        nums_length = len(nums)
        h = Heap(nums, nums_length)
        h.heapify()
        for i in xrange(k):
            h.extract_max()
        return nums[nums_length - k]

print(Solution().findKthLargest([3, 2, 1, 6, 5, 4], 1))

