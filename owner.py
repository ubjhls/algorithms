bingo = [list(map(int, input().split())) for _ in range(5)]
host = [list(map(int, input().split())) for _ in range(5)]


def bingo_result(arr):
    bingoCount = 0
    for Py in range(5):
        if (arr[Py][0] == arr[Py][1] == arr[Py][2] == arr[Py][3] == arr[Py][4] == 0):
            bingoCount += 1

    for Px in range(5):
        if (arr[0][Px] == arr[1][Px] == arr[2][Px] == arr[3][Px] == arr[4][Px] == 0):
            bingoCount += 1

    if (arr[0][0] == arr[1][1] == arr[2][2] == arr[3][3] == arr[4][4] == 0):
        bingoCount += 1

    if (arr[0][4] == arr[1][3] == arr[2][2] == arr[3][1] == arr[4][0] == 0):
        bingoCount += 1
    return bingoCount


count = 0
for i in range(5):
    for j in range(5):
        tmp = host[i][j]
        for k in range(5):
            for q in range(5):
                if bingo[k][q] == tmp:
                    bingo[k][q] = 0
                    count += 1
        if bingo_result(bingo) == 3:
            break
    if bingo_result(bingo) == 3:
        print(count)
        break