def dfs(x, y):
    global count

    for j in range(3):
        nx, ny = x + dx[j], y + dy[j]
        if nx < 0 or nx >= r:
            continue
        if arr[nx][ny] == 'x':
            continue
        if ny == c-1:
            count += 1
            return
        if not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny)


r, c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
count = 0
dx = [-1, 0, 1]
dy = [1, 1, 1]
for i in range(r):
    dfs(i, 0)
print(count)