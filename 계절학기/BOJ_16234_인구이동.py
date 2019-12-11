from collections import deque
def problem():
    global value, visit, tmp, count, mot
    visit = [[False] * N for _ in range(N)]
    tmp = []
    value = 0
    mot = 0
    for i in range(N):
        for j in range(N):
            for w in range(4):
                wi, wj = i + dx[w], j + dy[w]
                if wi < 0 or wj < 0 or wi >= N or wj >= N:
                    continue
                if L <= abs(arr[i][j] - arr[wi][wj]) <= R:
                    bfs(i, j)
                    value = sum(tmp) // len(tmp)
                    change()
                    count += 1
                    mot = 1
                    for m in range(4):
                        print(arr[m])
                    print(tmp)
                    return

def bfs(x, y):
    global q
    q = deque()
    visit[x][y] = True
    q.append((x, y))
    tmp.append(arr[x][y])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if L <= abs(arr[x][y] - arr[nx][ny]) <= R and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = True
                tmp.append(arr[nx][ny])

def change():
    global value
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                arr[i][j] = value

N, L, R = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
tmp = []
value = 0
count = 0
mot = 0
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
problem()
while True:
    problem()
    if mot == 0:
        break
print(count)