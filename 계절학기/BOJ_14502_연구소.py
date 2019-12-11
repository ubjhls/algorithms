from collections import deque
def bfs():
    for o in range(n):
        for p in range(m):
            if arr[o][p] == 2:
                q.append((o, p))
                visit[o][p] = True
                while q:
                    x, y = q.popleft()
                    for r in range(4):
                        nx, ny = x + dx[r], y + dy[r]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if arr[nx][ny] == 0 and not visit[nx][ny]:
                            q.append((nx, ny))
                            visit[nx][ny] = True


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
value = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            continue
        if arr[i][j] == 0:
            arr[i][j] = 1
        for k in range(i, n, 1):
            for w in range(m):
                if arr[k][w] != 0:
                    continue
                if arr[k][w] == 0:
                    arr[k][w] = 1
                for y in range(k, n, 1):
                    for u in range(m):
                        if arr[y][u] == 0:
                            arr[y][u] = 1
                            visit = [[False] * m for _ in range(n)]
                            bfs()
                            count = 0
                            for c in range(n):
                                for v in range(m):
                                    if arr[c][v] == 0 and not visit[c][v]:
                                        count += 1

                            if value < count:
                                value = count
                            arr[y][u] = 0
                arr[k][w] = 0
        arr[i][j] = 0
print(value)