def dfs(x, y, d):
    global count
    if arr[x][y] == 0:
        count += 1
        arr[x][y] = 1
    if d == 0:
        d = 3
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):                    # 북 : (-1, 0) 서 (0, -1) 남 (1, 0) 동 (0, 1)
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1:
                continue
            dfs(nx, ny, d)
            return
    elif d == 1:
        d = 0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1:
                continue
            dfs(nx, ny, d)
            return
    elif d == 2:

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1:
                continue

            dfs(nx, ny, d)
            return
    elif d == 3:
        d = 2
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1:
                continue
            dfs(nx, ny, d)
            return


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0
dfs(r, c, d)
print(count)