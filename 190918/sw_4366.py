T = int(input())
for i in range(T):
    tmp_1 = 0
    tmp_2 = 0
    result = 0
    two_tmp = []
    three_tmp = []
    two = input()
    three = input()
    for j in range(len(two)):
        tmp_1 += int(two[j]) * 2 ** (len(two)-1-j)
    for j in range(len(three)):
        tmp_2 += int(three[j]) * 3 ** (len(three)-1-j)
    for k in range(len(two)):
        ex_1 = tmp_1 + 2**k
        two_tmp.append(ex_1)
        ex_2 = tmp_1 - 2**k
        two_tmp.append(ex_2)
    for k in range(len(three)):
        ex_1 = tmp_2 + 3**k
        three_tmp.append(ex_1)
        ex_2 = tmp_2 - 3**k
        three_tmp.append(ex_2)
        ex_3 = tmp_2 + 2*(3**k)
        three_tmp.append(ex_3)
        ex_4 = tmp_2 - 2*(3**k)
        three_tmp.append(ex_4)
    for m in range(len(two_tmp)):
        for n in range(len(three_tmp)):
            if two_tmp[m] == three_tmp[n]:
                result += two_tmp[m]
                break
        if result:
            break
    print('#{} {}'.format(i+1, result))