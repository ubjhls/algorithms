def dfs(x, y, count, tmp):
    global result
    if count == 7:
        if tmp not in result:
            result.add(tmp)
            return
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= 4 or ny < 0 or ny >=4:
            continue
        dfs(nx, ny, count + 1, tmp + str(arr[nx][ny]))


T = int(input())
for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = set()
    for j in range(4):
        for k in range(4):
            count = 0
            tmp = ''
            dfs(j, k, count, tmp)
    print('#{} {}'.format(t, len(result)))