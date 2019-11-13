def dfs(x, y):
    global count
    if visit[y][x] == 1:
        return
    visit[y][x] = 1
    q.append((x, y))
    while q:
        x, y = q.pop()
        for j in range(4):
            tmp_x, tmp_y = x + dx[j], y + dy[j]
            if 0 <= tmp_x < M and 0 <= tmp_y < N:
                if arr[tmp_y][tmp_x] == 1 and visit[tmp_y][tmp_x] == 0:
                    q.append((tmp_x, tmp_y))
                    visit[tmp_y][tmp_x] = 1
                    break
    count += 1


T = int(input())
for m in range(T):
    M, N, K = map(int, input().split())
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    arr = [[0] * M for _ in range(N)]
    count = 0
    visit = [[0] * (M+1) for _ in range(N + 1)]
    q = []
    tmp = []
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
        tmp.append((x, y))
    for i in range(K):
        ex, ey = tmp.pop()
        dfs(ex, ey)
    print(count)
