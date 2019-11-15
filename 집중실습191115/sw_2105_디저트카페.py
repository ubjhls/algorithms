from copy import deepcopy
def back(x, y, Y):
    global tmp, result
    if i + 1 == x and j - 1 == y:
        temp = deepcopy(tmp)
        result.append(temp)
        return
    for k in range(4):
        if k < Y:
            continue
        nx, ny = x + dx[k], y + dy[k]
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue

        if cafe[nx][ny] in tmp:
            continue
        tmp.append(cafe[nx][ny])
        back(nx, ny, k)
        tmp.pop()


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    result = []
    max_value = 0
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1:
                continue
            tmp = []
            tmp.append(cafe[i][j])
            back(i, j, 0)
    for i in result:
        if max_value < len(i):
            max_value = len(i)
    if max_value < 4:
        max_value = -1

    print('#{} {}'.format(t, max_value))