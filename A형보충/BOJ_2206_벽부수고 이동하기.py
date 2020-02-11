import heapq

def bfs():
    q = []
    heapq.heappush(q, [1, 0, 0, 0])
    v[0][0][0] = True
    while q:
        d, i, j, c = heapq.heappop(q)
        if i == N-1 and j == M-1:
            return d
        for a in range(4):
            ni, nj = i+di[a], j+dj[a]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj][c]:
                v[ni][nj][c] = True
                if r[ni][nj] == '0':
                    heapq.heappush(q, [d+1, ni, nj, c])
                if r[ni][nj] == '1' and c == 0:
                    heapq.heappush(q, [d+1, ni, nj, 1])
    return -1

N, M = map(int, input().split())
r = [input() for _ in range(N)]
v = [[[False]*2 for _ in range(M)] for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
print(bfs())