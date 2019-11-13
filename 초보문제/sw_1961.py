import copy
testcase = int(input())

for i in range(testcase):
    test = int(input())
    arr = [list(map(int, input().split())) for _ in range(test)]
    arr_tmp1 = copy.deepcopy(arr)
    arr_tmp2 = copy.deepcopy(arr)
    arr_tmp3 = copy.deepcopy(arr)
    print('#{}'.format(i+1))
    for j in range(test):
        for k in range(test):
            arr_tmp1[j][k] = arr[-1-k][j]


    for j in range(test):
        for k in range(test):
            arr_tmp2[j][k] = arr[-1-j][-1-k]

    for j in range(test):
        for k in range(test):
            arr_tmp3[j][k] = arr[k][-1-j]

    for j in range(test):
        tmp_1 = ''
        tmp_2 = ''
        tmp_3 = ''
        for k in range(test):
            tmp_1 += str(arr_tmp1[j][k])
            tmp_2 += str(arr_tmp2[j][k])
            tmp_3 += str(arr_tmp3[j][k])
        print('{} {} {}'.format(tmp_1, tmp_2, tmp_3))