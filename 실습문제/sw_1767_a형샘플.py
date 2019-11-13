def back(x, y):
    visit[x][y] = True

    nx, ny = x + dx[k], y + dy[k]
    if arr[nx][ny] == 0:
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            visit[nx][ny] = True
            back(nx + k, ny + k)
            visit[nx][ny] = False



T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if i == n-1 or i == 0 or j == n-1 or j == 0:
                continue
            if arr[i][j] == 1:
                k = 1
                back(i, j)