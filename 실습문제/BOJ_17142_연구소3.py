from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(q):
    global count, arr
    arr = deepcopy(hospital)
    visit = [[False] * N for _ in range(N)]
    count = 0
    q = deque(q)
    while q:
        for i in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 1:
                    continue

                if arr[nx][ny] == 2:
                    visit[nx][ny] = True

                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    arr[nx][ny] = 2
        count += 1

def viruses():
    global result, arr
    for i in combinations(virus, M):
        tmp = 0
        bfs(i)
        for j in range(N):
            for k in range(N):
                if not arr[j][k]:
                    tmp += 1
        if tmp > 0:
            continue
        if result > count:
            result = count

N, M = map(int, input().split())
hospital = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
virus = deque()
count = 0
result = 0xffffff
arr = deepcopy(hospital)
for i in range(N):
    for j in range(N):
        if hospital[i][j] == 2:
             virus.append((i, j))
viruses()
if result == 0xffffff:
    result = 0
print(result - 1)
