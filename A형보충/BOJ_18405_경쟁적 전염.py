from collections import deque
from copy import deepcopy
def bfs():
    global count
    while q:
        if count == S:
            return
        for p in range(len(q)):
            virus, x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if arr[nx][ny] == 0:
                    arr[nx][ny] = virus
                    q.append((virus, nx, ny))
        count += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
S, X, Y = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            q.append((arr[i][j], i, j))
q = deque(sorted(q))
bfs()
print(arr[X - 1][Y - 1])
