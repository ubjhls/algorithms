from copy import deepcopy

def cal(x, y):
    tmp = block[y][x]
    block[y][x] = 0
    global W, H
    for n in range(1, tmp):
        if y + n >= H:
            break
        cal(x, y + n)

    for k in range(1, tmp):
        if y - k < 0:
            break
        cal(x, y - k)

    for m in range(1, tmp):
        if x + m >= W:
            break
        cal(x + m, y)

    for l in range(1, tmp):
        if x - l < 0:
            break
        cal(x - l, y)

def down():
    for _ in range(H):
        for k in range(W):
            for l in range(H-2, -1, -1):
                if block[l+1][k] == 0:
                    block[l+1][k] = block[l][k]
                    block[l][k] = 0

def min_value():
    global result
    element_count = 0
    for u in range(H):
        for y in range(W):
            if block[u][y] != 0:
                element_count += 1

    if result >= element_count:
        result = element_count

def check(count):
    global block
    if count == N:
        min_value()
        return
    for i in range(W):
        for j in range(H):
            if block[j][i]:
                tmp_block = deepcopy(block)
                cal(i, j)
                down()
                check(count + 1)
                block = tmp_block
                break
T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    count = 0
    result = 0xffffff
    check(count)
    if result == 0xffffff:
        result = 0
    print('#{} {}'.format(t, result))