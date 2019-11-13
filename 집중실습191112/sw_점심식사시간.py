def bfs(x, y):
    global time
    visit[x][y] = True
    q.append((x, y))
    while q:
        for p in range(len(q)):
            x, y = q.pop(0)
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if stair[nx][ny] != 0 and stair[nx][ny] != 1:
                    tmp.append((nx, ny))
                    return
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
        time += 1


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    stair = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    tmp = []
    time = 0
    for i in range(n):
        for j in range(n):
            if stair[i][j] == 1:
                visit = [[False] * n for _ in range(n)]
                bfs(i, j)
    print(tmp)