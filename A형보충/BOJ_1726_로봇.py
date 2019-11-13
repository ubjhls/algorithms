def dfs(x, y, d, count):
    global result
    if x == e_x - 1 and y == e_y - 1:
        if d != e_d:
            count += 1
        if result > count:
            result = count
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visit[nx][ny] and arr[nx][ny] == 0:
            visit[nx][ny] = True
            if d != i:
                sub_count = 1
                dfs(nx, ny, i, count + sub_count + 1)
                visit[nx][ny] = False
            else:
                dfs(nx, ny, i, count)
                visit[nx][ny] = False

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s_x, s_y, s_d = map(int, input().split())
e_x, e_y, e_d = map(int, input().split())
q = []
result = 1000
count = 0
visit = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit[s_x - 1][s_y - 1] = True
dfs(s_x - 1, s_y - 1, s_d, count)
print(result)