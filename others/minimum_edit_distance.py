__author__ = 'richard'


UPDATE_COST = 3
INSERT_COST = 8
DELETE_COST = 1
APPEND_COST = 2


def edit_distance(from_arr, from_arr_len, to_arr, to_arr_len):
    m = [[None for _ in xrange(to_arr_len + 1)] for _ in xrange(from_arr_len + 1)]

    m[0][0] = ('', 0)
    for i in xrange(1, to_arr_len + 1):
        m[0][i] = ('a' * i, i * APPEND_COST)

    for i in xrange(1, from_arr_len + 1):
        m[i][0] = ('d' * i, i * DELETE_COST)

    for i in xrange(1, from_arr_len + 1):
        for j in xrange(1, to_arr_len + 1):
            if from_arr[from_arr_len - i] == to_arr[to_arr_len - j]:
                m[i][j] = m[i - 1][j - 1]
            else:
                update_cost = (m[i - 1][j - 1][0] + 'u', m[i - 1][j - 1][1] + UPDATE_COST)
                insert_cost = (m[i][j - 1][0] + 'i', m[i][j - 1][1] + INSERT_COST)
                delete_cost = (m[i - 1][j][0] + 'd', m[i - 1][j][1] + DELETE_COST)
                m[i][j] = min([update_cost, insert_cost, delete_cost], key=lambda v: v[1])
    return m[from_arr_len - 1][to_arr_len - 1]

ts1 = 'An autopsy determied that the dexth of Samuel Harr11ell at the Fishill Correctional'
ts2 = 'An autopsy determined that the death of Samuel Harrell at the Fishkill Correctional AAA'
ts1_len = len(ts1)
ts2_len = len(ts2)
print(edit_distance(ts1, ts1_len, ts2, ts2_len))