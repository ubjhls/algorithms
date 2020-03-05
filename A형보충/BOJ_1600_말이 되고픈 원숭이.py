import collections

def bfs(i, j, k, dist):
    q = collections.deque()
    q.append([i, j, k, dist])
    visited[i][j] |= 1 << k

    while q:
        i, j, k, dist = q.popleft()
        if i == H-1 and j == W-1:
            return dist
        for a in range(12):
            if k == 0 and a >= 4:
                continue
            ni, nj = i+di[a], j+dj[a]
            if 0 <= ni < H and 0 <= nj < W and not board[ni][nj]:
                if a >= 4:
                    if not visited[ni][nj] & 1 << k-1:
                        visited[ni][nj] |= 1 << (k-1)
                        q.append([ni, nj, k-1, dist+1])
                else:
                    if not visited[ni][nj] & 1 << k:
                        visited[ni][nj] |= 1 << k
                        q.append([ni, nj, k, dist+1])
    return -1

K = int(input())
W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]
visited = [[0]*W for _ in range(H)]
di = [0, 0, -1, 1, -2, -2, 2, 2, -1, 1, -1, 1]
dj = [-1, 1, 0, 0, -1, 1, -1, 1, -2, -2, 2, 2]

print(bfs(0, 0, K, 0))