from collections import deque

def bfs():
    while q:
        d = q.popleft()
        if d == 123456789:
            print(dist[d])
            return
        s = str(d)
        k = s.find('9')
        x, y = k//3, k%3
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            nk = nx*3 + ny
            ns = list(s)
            ns[k], ns[nk] = ns[nk], ns[k]
            nd = int(''.join(ns))
            if not dist.get(nd):
                dist[nd] = dist[d]+1
                q.append(nd)
    print(-1)

q = deque()
dist = dict()
a = [list(map(int, input().split())) for _ in range(3)]
m = 0
for i in range(3):
    for j in range(3):
        n = a[i][j]
        if not n:
            n = 9
        m = m*10 + n
q.append(m)
dist[m] = 0
bfs()
