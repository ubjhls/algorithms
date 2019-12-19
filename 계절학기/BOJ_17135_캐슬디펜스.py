from heapq import heappush, heappop
from copy import deepcopy

def turn(arr2):
    cnt = 0
    for _ in range(n):
        v = []
        for k in range(3):
            q = []
            for i in range(n):
                for j in range(m):
                    if arr2[i][j]:
                        dist = abs(n - i) + abs(archer[k] - j)
                        if dist <= d:
                            heappush(q, (dist, j, i))
            if q:
                t, y, x = heappop(q)
                v.append((x, y))
        for x, y in v:
            if arr2[x][y]:
                arr2[x][y] = 0
                cnt += 1
        for i in range(n-2, -1, -1):
            for j in range(m):
                arr2[i+1][j] = arr2[i][j]
        for i in range(m):
            arr2[0][i] = 0
    return cnt

n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
archer = [0] * 3
ans = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            archer[0], archer[1], archer[2] = i, j, k
            arr2 = deepcopy(arr)
            ans = max(ans, turn(arr2))
print(ans)