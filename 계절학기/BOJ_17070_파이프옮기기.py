def dfs(x, y, dir):
    global count
    if x == n-1 and y == n-1:
        count += 1
        return
    if dir == 0:
        for k in range(2):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if k == 1:
                if visit[nx - 1][ny] == True or visit[nx][ny - 1] == True:
                    continue
            visit[nx][ny] = True
            dfs(nx, ny, k)
            visit[nx][ny] = False
    elif dir == 2:
        for k in range(1, 3, 1):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if k == 1:
                if visit[nx - 1][ny] == True or visit[nx][ny - 1] == True:
                    continue
            visit[nx][ny] = True
            dfs(nx, ny, k)
            visit[nx][ny] = False
    else:
        for k in range(3):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if k == 1:
                if visit[nx - 1][ny] == True or visit[nx][ny - 1] == True:
                    continue
            visit[nx][ny] = True
            dfs(nx, ny, k)
            visit[nx][ny] = False

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
visit[0][0] = True
visit[0][1] = True
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            visit[i][j] = True
count = 0
dx = [0, 1, 1]
dy = [1, 1, 0]
dfs(0, 1, 0)
print(count)