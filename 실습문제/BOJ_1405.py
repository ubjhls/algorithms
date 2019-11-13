def dfs(x, y):
    global tmp, count
    visit[y][x] = True
    tmp_x = x
    tmp_y = y
    for i in range(4):
        if count == 0:
            tmp = 1
        nx, ny = tmp_x + dx[i], tmp_y + dy[i]
        if count == per[0]:
            result.append(tmp)
            tmp /= per[i + 1]
            return
        else:
            if not visit[ny][nx]:
                tmp *= per[i + 1]
                count += 1
                visit[ny][nx] = True
                dfs(nx, ny)
                visit[ny][nx] = False
                count -= 1


per = list(map(int, input().split()))
for i in range(1, len(per)):
    per[i] = per[i] / 100
visit = [[False] * 30 for _ in range(30)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tmp = 1
count = 0
result = []
dfs(15,15)
print(round(sum(result),9))