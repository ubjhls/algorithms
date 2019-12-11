from collections import deque
def bfs(x, y):
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if arr[nx][ny] == 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny))

def check(x, y):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if arr[nx][ny] == 0 and visit[nx][ny]:
            visit[x][y] = True
            return

def remove():
    global mot
    mot = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visit[i][j]:
                arr[i][j] = 0
                mot = 1

def solve():
    global count, visit, mot, time, result
    while True:
        visit = [[False] * M for _ in range(N)]
        bfs(0, 0)
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1:
                    check(i, j)
        remove()
        if mot == 0:
            return
        for i in range(N):
            count += arr[i].count(1)
        if count != 0:
            result = count
        print(result)
        time += 1
        count = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[False] * M for _ in range(N)]
result = 0
time = 0
count = 0
mot = 0
solve()
print(time)
print(result)