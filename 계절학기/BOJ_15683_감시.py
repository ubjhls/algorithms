def cal(x, y, i, cnt):
    for j in i:
        nx, ny = x + dx[j], y + dy[j]
        while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
            visit[nx][ny] += cnt
            nx, ny = nx + dx[j], ny + dy[j]

def back(n, k):
    global count, min_value
    if n == k:
        count = 0
        for o in range(N):
            for p in range(M):
                if arr[o][p] == 0 and visit[o][p] == 0:
                    count += 1
        if min_value > count:
            min_value = count
    else:
        x, y, d = cctv[n]
        for i in dir[d]:
            cal(x, y, i, 1)
            back(n + 1, k)
            cal(x, y, i, -1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
cctv = []
dir = [[], [[0], [1], [2], [3]], [(0, 2), (1, 3)], [(0, 1), (1, 2), (2, 3), (0, 3)],
      [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)], [(0, 1, 2, 3)]]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0
min_value = N * M
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append((i, j, arr[i][j]))
back(0, len(cctv))
print(min_value)