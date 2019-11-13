def back(x, y, angle):
    global result
    if x == n - 1 and y == n - 1:
        result += 1
    for i in range(3):
        if i + angle == 1:
            continue
        tmp_x, tmp_y = x + dx[i], y + dy[i]
        if tmp_x >= n or tmp_y >= n or arr[tmp_x][tmp_y]:
            continue
        if i == 2 and (arr[x][y + 1] or arr[x + 1][y]):
            continue
        back(tmp_x, tmp_y, i)
    return result

dx, dy = (0, 1, 1), (1, 0, 1)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
print(back(0, 1, 0))