from collections import deque
def bfs():
    while q:
        x, y = q.popleft()
        if arr[1][x][y] == 0:
            continue
        arr[1][x][y] -= 1
        if arr[0][x][y] > arr[1][x][y]:
            for m in range(4):
                nx, ny = x + dx[m], y + dy[m]
                if arr[0][nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    arr[0][nx][ny] = arr[0][x][y]
                    arr[1][nx][ny] = 2 * arr[0][x][y]

def start():
    global max_value
    for k in range(N):
        for l in range(M):
            if cell[k][l] > max_value:
                max_value = cell[k][l]
            visit[cover+k][cover+l] = True
            arr[0][cover+k][cover+l] = cell[k][l]
            arr[1][cover+k][cover+l] = 2 * cell[k][l]
            if arr[0][cover+k][cover+l] == 0:
                visit[cover+k][cover+l] = False
    return

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    cover = (2 * K) // 2
    b = K
    num = 0
    cell = [list(map(int, input().split())) for _ in range(N)]
    arr = [[[0] * (M + (2 * K)) for _ in range(N + (2 * K))] for _ in range(2)]
    visit = [[False] * (M + (2 * K)) for _ in range(N + (2 * K))]
    q = deque()
    count = 0
    max_value = 0
    dx = [0, 0, 1, -1]
    start()
    while b:
        num += 1
        b = b - 1
        for l in range(max_value, 0, -1):
            for i in range(cover - num, cover + N + num, 1):
                for j in range(cover - num, cover + M + num, 1):
                    if visit[i][j] == True and arr[1][i][j] == 0:
                        arr[0][i][j] = 0
                    if arr[0][i][j] == l:
                        q.append((i, j))
        bfs()

    for i in range(N + (2 * K)):
        for j in range(M + (2 * K)):
            if arr[1][i][j]:
                count += 1
    print('#{} {}'.format(t, count))
