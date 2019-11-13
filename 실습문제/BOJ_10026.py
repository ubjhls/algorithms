import sys; sys.setrecursionlimit(10000)
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[nx][ny] == arr[x][y] and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny)

N = int(input())
arr = [input() for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count_1 = 0
count_2 = 0
visit = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            count_1 += 1
            dfs(i, j)
visit = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    arr[i] = arr[i].replace('G', 'R')
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            count_2 += 1
            dfs(i, j)
print(count_1, count_2)