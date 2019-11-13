def dfs(y, x):
    count = 0
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if castle[ny][nx] == '.':
            count += 1
    if count >= castle[y][x]:
        castle[y][x] = '.'
    return

h, w = map(int, input().split())
castle = list(input() for _ in range(h))

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
result = 0
