def dfs(x, y, time):
    global result
    if dp[x][y] > time:
        dp[x][y] = time
    else:
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if nx == n-1 and ny == n-1:
            if result >= time:
                result = time
            return
        if not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny, time + int(load[nx][ny]))
            visit[nx][ny] = False


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    result = 0xfffff
    visit = [[False] * n for _ in range(n)]
    dp = [[0xffff] * n for _ in range(n)]
    load = [list(input()) for _ in range(n)]
    dfs(0, 0, 0)
    print('#{} {}'.format(t, result))