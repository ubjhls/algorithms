from collections import deque
def bfs(x, y):
    global count
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if bomb[nx][ny] == '.' and not visit[nx][ny]:
                visit[nx][ny] = True
                check_2(nx, ny)
def check(x, y):
    global count
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if bomb[nx][ny] == '*':
            return
    q.append((x, y))
    bfs(x, y)
    count += 1

def check_2(nx, ny):
    for w in range(8):
        tx, ty = nx + dx[w], ny + dy[w]
        if tx < 0 or ty < 0 or tx >= N or ty >= N:
            continue
        if bomb[tx][ty] == '*':
            return
    q.append((nx, ny))


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    bomb = [list(map(str, input())) for _ in range(N)]
    dx = [-1, 0, 1, 1, -1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    count = 0
    visit = [[False] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '*':
                visit[i][j] = True

    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '.' and not visit[i][j]:
                check(i, j)

    for i in range(N):
        for j in range(N):
            if visit[i][j] == False:
                count += 1

    print('#{} {}'.format(t, count))