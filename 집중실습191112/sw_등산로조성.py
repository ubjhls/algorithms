def dfs(x, y, count):
    global result
    if result < count:
        result = count
    visit[x][y] = True
    for p in range(4):
        nx, ny = x + dx[p], y + dy[p]
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue
        if not visit[nx][ny] and mountain[nx][ny] < mountain[x][y]:
            visit[nx][ny] = True
            dfs(nx, ny, count + 1)
            visit[nx][ny] = False

T = int(input())
for t in range(1, T + 1):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    max_ans = max(list(map(max, mountain)))
    result = 0
    for i in range(n):
        for j in range(n):
            for y in range(1, k + 1):
                tmp = mountain[i][j]
                mountain[i][j] -= y
                if mountain[i][j] < 0:
                    mountain[i][j] = 0
                for q in range(n):
                    for w in range(n):
                        count = 1
                        visit = [[False] * n for _ in range(n)]
                        if mountain[q][w] == max_ans:
                            dfs(q, w, count)
                mountain[i][j] = tmp
    print('#{} {}'.format(t, result))