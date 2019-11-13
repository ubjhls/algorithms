def bfs():
    global count
    while q:
        for w in range(len(q)):
            x, y = q.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if not visit[nx][ny] and arr[nx][ny] == 0:
                    visit[nx][ny] = True
                    q.append((nx, ny))
        count += 1
        if x == n - 1 and y == m - 1:
            return
    count = 10000
    return

n, m = map(int, input().split())
arr_tmp = [input() for _ in range(n)]
arr = [[0] * m for _ in range(n)]
for j in range(n):
    for k in range(m):
        arr[j][k] = int(arr_tmp[j][k])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = []
result = []
count = 0
visit = [[False] * m for _ in range(n)]
visit[0][0] = True
q.append((0, 0))
bfs()
ex = 0
result = 10000
for j in range(n):
    for k in range(m):
        visit = [[False] * m for _ in range(n)]
        count = 0
        ex = 0
        if 1 <= j < n - 1 and 1 <= k < m - 1:
            for i in range(4):
                nj, nk = j + dx[i], k + dy[i]
                if arr[nj][nk] == 0:
                    ex += 1
            if ex >= 2 and arr[j][k] == 1:
                arr[j][k] = 0
                visit[0][0] = True
                q.append((0, 0))
                bfs()
                arr[j][k] = 1
                if count < result:
                    result = count
if result != 10000:
    print(result)
else:
    print(-1)