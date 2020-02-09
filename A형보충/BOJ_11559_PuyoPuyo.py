import collections

def bfs(i, j):
    color = board[i][j]
    q = collections.deque()
    pos = []
    visited[i][j] = True
    cnt = 1
    q.append((i, j))
    pos.append((i, j))

    while q:
        i, j = q.popleft()
        for a in range(4):
            ni, nj = i+di[a], j+dj[a]
            if 0 <= ni < 6 and 0 <= nj < 12 and not visited[ni][nj] and board[ni][nj] == color:
                visited[ni][nj] = True
                cnt += 1
                q.append((ni, nj))
                pos.append((ni, nj))
    if cnt >= 4:
        for p in pos:
            board[p[0]][p[1]] = '#'
        return True
    return False

def search():
    flag = False
    i = 0
    while i < 6:
        j = 0
        while j < 12:
            if board[i][j] != '.' and not visited[i][j]:
                if bfs(i, j):
                    flag = True
            j += 1
        i += 1
    return flag

def remove():
    i = 0
    while i < 6:
        j = 0
        while j < 12:
            visited[i][j] = False
            if board[i][j] == '#':
                board[i].pop(j)
                board[i].append('.')
                visited[i].pop(j)
                visited[i].append(False)
                continue
            j += 1
        i += 1

board = [['.' for _ in range(12)] for _ in range(6)]
visited = [[False]*12 for _ in range(6)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
combo = 0
for j in range(11, -1, -1):
    data = input()
    for i in range(6):
        board[i][j] = data[i]

while True:
    state = search()
    if not state:
        break
    else:
        remove()
        combo += 1
print(combo)