def dfs(x, y, count):
    global tmp
    if tmp < count:
        tmp = count
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= num or ny < 0 or ny >= num:
            continue
        if arr[x][y] + 1 == arr[nx][ny]:
            dfs(nx, ny, count + 1)
    return tmp

T = int(input())

for t in range(1, T + 1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(num)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = [0, 1000]
    for i in range(num):
        for j in range(num):
            tmp = 0
            value = dfs(i, j, 1)
            index = arr[i][j]
            if result[0] < value:
                result = [value, index]
            elif result[0] == value:
                if result[1] > index:
                    result = [value, index]

    print('#{} {} {}'.format(t, result[1], result[0]))