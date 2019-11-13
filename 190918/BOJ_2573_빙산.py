import copy
def bfs(x, y):
    global cnt
    visit[x][y] = True
    q.append((x,y))
    while q:
        q.pop(0)
        for m in range(4):
            tmp_x, tmp_y = x + dx[m], + y + dy[m]
            if not visit[tmp_x][tmp_y]:
                visit[tmp_x][tmp_y] = True
                q.append((tmp_x, tmp_y))
    cnt += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = []
result = 0
while True:
    visit = [[False] * M for _ in range(N)]
    ex = copy.deepcopy(arr)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ex[i][j] != 0:
                count = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if ex[ni][nj] == 0:
                        count += 1
                if arr[i][j] - count <= 0:
                    arr[i][j] = 0
                else:
                    arr[i][j] = arr[i][j] - count
    print(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visit[i][j]:
                bfs(i, j)
    result += 1
    if cnt != 1:
        break
print(result)