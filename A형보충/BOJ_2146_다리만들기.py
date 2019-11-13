from collections import deque
def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 1 and visit[nx][ny] != color:
                visit[nx][ny] = color
                q.append((nx, ny))

n = int(input())
arr = [list(map(int, input())).split() for _ in range(n)]
visit = [[0] * n for _ in range(n)]
q = deque()
color = 2
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = color
            q.append((i, j))
            bfs()
            color += 1