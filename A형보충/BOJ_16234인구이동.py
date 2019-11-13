def bfs(x, y):
    global count
    q.append((x, y))
    tmp.append(arr[x][y])
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visit[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                visit[x][y] = True
                visit[nx][ny] = True
                q.append((nx, ny))
                tmp.append(arr[nx][ny])
                count = 1

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
q = []
while True:
    visit = [[False] * n for _ in range(n)]
    for w in range(n):
        for t in range(n):
            count = 0
            tmp = []
            if visit[w][t] == True:
                continue
            bfs(w, t)
            if count == 0:
                continue
            else:
                result.append(count)
                avg = sum(tmp) // len(tmp)
                for j in range(n):
                    for k in range(n):
                        if visit[j][k]:
                            arr[j][k] = avg

    if count == 0:
        break

print(sum(result))