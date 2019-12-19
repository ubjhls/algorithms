def dfs(x, y, d):
    global count
    if arr[x][y] == 1:
        return
    if arr[x][y] == 0:
        count += 1
        arr[x][y] = 2
    for o in range(n):
        print(arr[o])
    print('--------------------------------')
    if d == 0:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

    elif d == 1:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

    elif d == 2:
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

    elif d == 3:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
                                          # 0 북    1 동     2 남     3 서
    for i in range(4):                    # 북 : (-1, 0) 서 (0, -1) 남 (1, 0) 동 (0, 1)
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1 or arr[nx][ny] == 2:
            continue
        if dx[i] == 0 and dy[i] == -1:
            d = 3
            dfs(nx, ny, d)
        elif dx[i] == 1 and dy[i] == 0:
            d = 2
            dfs(nx, ny, d)
        elif dx[i] == 0 and dy[i] == 1:
            d = 1
            dfs(nx, ny, d)
        elif dx[i] == -1 and dy[i] == 0:
            d = 0
            dfs(nx, ny, d)
    return

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0
dfs(r, c, d)
print(count)