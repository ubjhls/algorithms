from heapq import heappush, heappop
from copy import deepcopy

n, m, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
archer = [0] * 3

def kill(b):
    cnt = 0
    for _ in range(n):
        v = []
        for k in range(3):
            q = []
            for i in range(n):
                for j in range(m):
                    if b[i][j]:
                        dist = abs(n - i) + abs(archer[k] - j)
                        if dist <= d:
                            heappush(q, (dist, j, i))
            if q:
                _, y, x = heappop(q)
                v.append((x, y))
        for x, y in v:
            if b[x][y]:
                b[x][y] = 0
                cnt += 1
        for i in range(n-2, -1, -1):
            for j in range(m):
                b[i+1][j] = b[i][j]
        for i in range(m):
            b[0][i] = 0
    return cnt

ans = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            archer[0], archer[1], archer[2] = i, j, k
            b = deepcopy(a)
            ans = max(ans, kill(b))
print(ans)