from collections import deque
def problem():
    global count
    global visit
    global visited
    result = 1
    while True:
        cnt = 0
        visit = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0:
                    count = 0
                    bfs(i, j)
        for i in range(n):
            for j in range(m):
                arr[i][j] = arr[i][j] - visit[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0 and not visited[i][j]:
                    cnt += 1
                    check(i, j)
        if cnt > 1:
            return result
        elif cnt == 0:
            return 0
        result += 1

def bfs(x, y):
    global count
    global visit
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if arr[nx][ny] == 0:
            count += 1
    visit[x][y] = count

def check(x, y):
    global visited
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx, ny = x + dx[w], y + dy[w]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] != 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0] * m for _ in range(n)]
q = deque()
count = 0
visit = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
print(problem())

