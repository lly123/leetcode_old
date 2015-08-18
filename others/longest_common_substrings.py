__author__ = 'richard'


def lcs(a1, a1_len, a2, a2_len):
    m = [[('', 0) for _ in xrange(a2_len + 1)] for _ in xrange(a1_len + 1)]
    for i in xrange(1, a1_len + 1):
        for j in xrange(1, a2_len + 1):
            if a1[i - 1] == a2[j - 1]:
                m[i][j] = (m[i - 1][j - 1][0] + a1[i - 1], m[i - 1][j - 1][1] + 1)
            else:
                m[i][j] = m[i][j - 1] if m[i][j - 1][1] > m[i - 1][j][1] else m[i - 1][j]
    return m[a1_len][a2_len]


arr1 = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
arr2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
print(lcs(arr1, len(arr1), arr2, len(arr2)))