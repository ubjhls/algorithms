def dfs(start_y, start_x):
    global count, n
    stack.append((start_y, start_x))
    visit[start_y][start_x] = 1
    while stack:
        start_y, start_x = stack.pop()
        for i in range(3):
            tmp_y, tmp_x = start_y + dy[i], start_x + dx[i]
            if tmp_x < n and tmp_y < n:
                if arr[tmp_y][tmp_x] == 5:
                    count += 1
                if arr[tmp_y][tmp_x] == 1:
                    continue
                elif arr[tmp_y - 1][tmp_x - 1] == 2 and arr[tmp_y - 1][tmp_x] == 0 and arr[tmp_y][tmp_x - 1] == 0:
                    if visit[tmp_y][tmp_x] == 0:
                        visit[tmp_y][tmp_x] == 1
                        stack.append((tmp_y, tmp_x))
                elif arr[tmp_y][tmp_x - 1] == 2:
                    if arr[tmp_y - 1][tmp_x - 1] == 2:
                        continue
                    else:
                        if visit[tmp_y][tmp_x] == 0:
                            visit[tmp_y][tmp_x] == 1
                            stack.append((tmp_y, tmp_x))
                elif arr[tmp_y - 1][tmp_x] == 2:
                    if arr[tmp_y - 1][tmp_x - 1] == 2:
                        continue
                    else:
                        if visit[tmp_y][tmp_x] == 0:
                            visit[tmp_y][tmp_x] == 1
                            stack.append((tmp_y, tmp_x))



n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
stack = []
count = 0
dx = [1, 1, 0]
dy = [0, 1, 1]
dfs(0, 1)
print(count)