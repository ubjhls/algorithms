def dfs(a, b):
    global count
    if visit[a][b] == 1:
        return
    visit[a][b] = 1
    q.append((a, b))
    while q:
        t, r = q.pop()
        for j in range(4):
            tmp_x, tmp_y = t + dx[j], r + dy[j]
            if 0 <= tmp_x < M and 0 <= tmp_y < N:
                if arr[tmp_x][tmp_y] == 1 and visit[tmp_x][tmp_y] == 0:
                    q.append((tmp_x, tmp_y))
                    visit[tmp_x][tmp_y] = 1
    count += 1


T = int(input())
for m in range(T):
    M, N, K = map(int, input().split())
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    arr = [[0] * N for _ in range(M)]
    count = 0
    visit = [[0] * (N+1) for _ in range(M + 1)]
    q = []
    tmp = []
    for i in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
        tmp.append((x, y))
    for i in range(K):
        ex, ey = tmp.pop()
        dfs(ex, ey)
    print(count)