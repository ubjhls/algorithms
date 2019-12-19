n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0
while True:
    tmp = 0
    if arr[r][c] == 1:
        break
    if arr[r][c] == 0:
        arr[r][c] = 2
        count += 1
    if d == 0:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

    elif d == 1:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

    elif d == 2:
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

    elif d == 3:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

    for i in range(4):                    # 북 : (-1, 0) 서 (0, -1) 남 (1, 0) 동 (0, 1)
        tmp += 1
        nx, ny = r + dx[i], c + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1 or arr[nx][ny] == 2:
            continue
        if dx[i] == 0 and dy[i] == -1:
            d = 3
            r = nx
            c = ny
            break
        elif dx[i] == 1 and dy[i] == 0:
            d = 2
            r = nx
            c = ny
            break
        elif dx[i] == 0 and dy[i] == 1:
            d = 1
            r = nx
            c = ny
            break
        elif dx[i] == -1 and dy[i] == 0:
            d = 0
            r = nx
            c = ny
            break
    if tmp == 4:
        if d == 0:
            r = r + 1
        elif d == 1:
            c = c - 1
        elif d == 2:
            r = r - 1
        elif d == 3:
            c = c + 1
print(count)