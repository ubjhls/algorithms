def bfs(x, y):
    global count
    visit[x][y] = True
    while q:
        for w in range(len(q)):
            x, y = q.pop(0)
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if not visit[nx][ny] and arr[nx][ny] == 'L':
                    visit[nx][ny] = True
                    q.append((nx, ny))
        count += 1


n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = []
result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visit = [[False] * m for _ in range(n)]
            count = 0
            q.append((i, j))
            bfs(i, j)
            print(count)
            result.append(count - 1)
print(max(result))