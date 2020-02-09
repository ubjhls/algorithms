import sys

def dfs(x, y, count, value):
    global ans
    for k in range(4):
        try:
            nx, ny = x + dx[k], y + dy[k]
        except IndexError:
            continue
        if not visit[nx][ny]:
            visit[nx][ny] = True
            if count == 4:
                if value > ans:
                    ans = value
                return
            dfs(nx, ny, count + 1, value + arr[nx][ny])
            visit[nx][ny] = False

def mid(x, y):
    global value, ans
    if x-1 >=0 and x+1 < n and y+1 < m:
        tmp = 0
        tmp = value + arr[x-1][y] + arr[x+1][y] + arr[x][y+1]
        if tmp > ans:
            ans = tmp
    if x-1 >=0 and x+1 < n and y-1 >= 0:
        tmp = 0
        tmp = value + arr[x - 1][y] + arr[x + 1][y] + arr[x][y - 1]
        if tmp > ans:
            ans = tmp
    if y+1 <m and y-1 >=0 and x+1 <n:
        tmp = 0
        tmp = value + arr[x][y + 1] + arr[x][y - 1] + arr[x + 1][y]
        if tmp > ans:
            ans = tmp
    if y+1 <m and y-1 >=0 and x-1>=0:
        tmp = 0
        tmp = value + arr[x][y + 1] + arr[x][y - 1] + arr[x - 1][y]
        if tmp > ans:
            ans = tmp

n, m = map(int, input().split())
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        visit = [[False] * m for _ in range(n)]
        count = 1
        value = arr[i][j]
        mid(i, j)
        dfs(i, j, count, value)
print(ans)