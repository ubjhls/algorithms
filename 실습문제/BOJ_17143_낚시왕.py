def move(y):
    global shark
    for k in range(R + 1):
        if arr[k][y][0]:
            shark += arr[k][y][3]
            arr[k][y] = 0
            break
        else:
            continue
    shark_move()
def shark_move():
    for i in range(R):
        for j in range(C):
            if arr[i][j]:
                nx, ny = i + dx[arr[i][j][2]], j + dy[arr[i][j][2]]


R, C, M = map(int, input().split())
arr = [[[0] for _ in range(C + 1)] for i in range(R + 1)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r][c].append(s)
    arr[r][c].append(d)
    arr[r][c].append(z)
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
shark = 0
# for j in range(1, C + 1, 1):
#     move(j)
print(arr)
print(arr[1][3])