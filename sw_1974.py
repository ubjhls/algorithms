import copy
testcase = int(input())
for i in range(testcase):
    sdoku = [list(map(int,input().split())) for _ in range(9)]

    for j in range(9):
        count = 0
        for k in range(9):
            if k+1 in sdoku[j]:
                count += 1
            else:
                break
        if count == 9:
            continue
        else:
            print('#{} {}'.format(i+1, 0))
            break
    if count != 9:
        continue
    sdoku_tmp = copy.deepcopy(sdoku)
    for o in range(9):
        for p in range(9):
            sdoku_tmp[o][p] = sdoku[p][o]

    for j in range(9):
        count = 0
        for k in range(9):
            if k+1 in sdoku_tmp[j]:
                count += 1
            else:
                break
        if count == 9:
            continue
        else:
            print('#{} {}'.format(i+1, 0))
            break
    if count != 9:
        continue

    for q in range(0,9,3):
        tmp = []
        for j in range(3):
            for k in range(3):
                tmp.append(sdoku[j+q][k+q])
        tmp = set(tmp)
        if len(tmp) < 9:
            print('#{} {}'.format(i + 1, 0))
            break
    if len(tmp) == 9:
        print('#{} {}'.format(i + 1, 1))