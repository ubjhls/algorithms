import copy
def bfs(x, y):
    global count, q
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.pop(0)
        for m in range(4):
            nx, ny = x + dx[m], y + dy[m]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visit[nx][ny] and ex[nx][ny] != 0:
                visit[nx][ny] = True
                q.append((nx, ny))
    count += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
tmp = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
count = 0
for i in range(len(arr)):
    tmp.append(max(arr[i]))
end = max(tmp)

for i in range(0, end + 1):
    count = 0
    ex = copy.deepcopy(arr)
    visit = [[False] * N for _ in range(N)]
    for j in range(len(arr)):
        for k in range(len(arr)):
            if ex[j][k] <= i:
                ex[j][k] = 0
    for p in range(len(arr)):
        for r in range(len(arr)):
            q = []
            if ex[p][r] != 0 and not visit[p][r]:
                bfs(p, r)
    if ans < count:
        ans = count
print(ans)