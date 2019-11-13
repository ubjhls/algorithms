from collections import deque

def bfs():
    global count
    while q:
        for u in range(len(q)):
            z, y, x = q.popleft()
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
                    continue
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = 1
                    q.append((nz, ny, nx))
        count += 1
    for j in range(h):
        for k in range(n):
            for l in range(m):
                if arr[j][k][l] == 0:
                    count = -1
                    return count
    return count

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[False] * m for _ in range(n)] for _ in range(h)]
result = 0
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()
count = -1
for j in range(h):
    for k in range(n):
        for l in range(m):
            if arr[j][k][l] == 1:
                q.append((j, k, l))


bfs()
print(count)