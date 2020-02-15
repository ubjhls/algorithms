import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
dist = [[[0]*64 for _ in range(m)] for _ in range(n)]
q = deque()

def init():
    for i in range(n):
        for j in range(m):
            if a[i][j] == '0':
                q.append((i, j, 0))
                return

def bfs():
    while q:
        x, y, k = q.popleft()
        if a[x][y] == '1':
            print(dist[x][y][k])
            return
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny, nk = x+dx, y+dy, k
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            c = a[nx][ny]
            if c.islower():
                nk |= (1<<(ord(c)-ord('a')))
            elif c.isupper() and not nk & (1<<(ord(c)-ord('A'))):
                continue
            if not dist[nx][ny][nk] and c != '#':
                q.append((nx, ny, nk))
                dist[nx][ny][nk] = dist[x][y][k] + 1
    print(-1)

init()
bfs()
