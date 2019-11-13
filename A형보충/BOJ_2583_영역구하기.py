import sys; sys.setrecursionlimit(100000)

def dfs(y, x):
    global count
    visit[y][x] = True
    for w in range(4):
        nx, ny = x + dx[w], y + dy[w]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not visit[ny][nx]:
            visit[ny][nx] = True
            count += 1
            dfs(ny, nx)

m, n, k = map(int,input().split())
arr = [[0] * n for _ in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
ans = 0
visit = [[False] * n for _ in range(m)]

for i in range(k):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for j in range(x_1, x_2, 1):
        for k in range(y_1, y_2, 1):
            arr[k][j] = 1
            visit[k][j] = True

for j in range(n):
    for k in range(m):
        if arr[k][j] == 0 and not visit[k][j]:
            ans += 1
            count = 1
            dfs(k, j)
            result.append(count)
print(ans)
print(result)