__author__ = 'richard'


from multiprocessing import Pool
MAX_PARALLEL_PROCESS_NUM = 4


def parallel_sum(p):
    return [p[0], sum(p[1][:])]


def sweep(args):
    data_arr, root, children = args
    ret = [data_arr[root]]
    for i in xrange(1, len(children)):
        ret.append(ret[i - 1] + data_arr[children[i - 1]])
    return ret


class ParallelPrefixSum:
    def __init__(self, data_arr):
        self.pool = Pool(MAX_PARALLEL_PROCESS_NUM)
        self.original_data_arr = data_arr
        self.original_data_arr_len = len(data_arr)
        self.roots = []

    def up_sweep(self):
        def partition(parallel_num):
            begin = 0
            while begin < data_arr_len:
                end = begin + (parallel_num - 1) if begin + (parallel_num - 1) < data_arr_len else data_arr_len - 1
                yield ([index_arr[x] for x in xrange(begin, end + 1)], data_arr[begin:end + 1])
                begin += parallel_num

        data_arr = self.original_data_arr
        data_arr_len = self.original_data_arr_len
        index_arr = xrange(data_arr_len)
        while data_arr_len > 1:
            ret = self.pool.map(parallel_sum, partition(3))
            index_arr = []
            data_arr = []
            data_arr_len = 0
            self.roots.append([])
            for r in ret:
                self.original_data_arr[r[0][-1]] = r[1]
                index_arr.append(r[0][-1])
                data_arr.append(r[1])
                data_arr_len += 1
                self.roots[-1].append((self.original_data_arr, r[0][-1], r[0]))

    def down_sweep(self):
        self.original_data_arr[-1] = 0
        parts = self.roots.pop()
        while parts:
            r = self.pool.map(sweep, parts)
            for i in xrange(0, len(parts)):
                for j in zip(parts[i][2], r[i]):
                    self.original_data_arr[j[0]] = j[1]
            parts = self.roots.pop() if self.roots else None

    def run(self):
        self.up_sweep()
        self.down_sweep()
        return self.original_data_arr

arr = [10, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = ParallelPrefixSum(arr).run()
print(a)