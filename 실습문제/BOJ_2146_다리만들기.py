from copy import deepcopy
def bfs(x, y):
    global count, ans
    visit_2[x][y] = True
    q.append((x, y))
    while q:
        if count >= ans:
            return
        for t in range(len(q)):
            x, y = q.pop(0)
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if arr[nx][ny] != 0 and arr[nx][ny] != ex:
                    if ans > count:
                        ans = count
                        return
                    else:
                        return
                if not visit_2[nx][ny] and arr[nx][ny] == 0:
                    visit_2[nx][ny] = True
                    q.append((nx, ny))
        count += 1
def visit_check(x, y):
    visit[x][y] = True
    arr[x][y] = ex
    tmp.append((x, y))
    while tmp:
        x, y = tmp.pop(0)
        for w in range(4):
            nx, ny = x + dx[w], y + dy[w]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visit[nx][ny] and arr[nx][ny] != 0:
                visit[nx][ny] = True
                arr[nx][ny] = ex
                tmp.append((nx, ny))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[False] * n for _ in range(n)]
tmp = []
ans = 10000
ex = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and not visit[i][j]:
            ex += 1
            visit_check(i, j)

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and (i == 0 or j == 0 or i == n-1 or j == n-1):
            visit_2 = deepcopy(visit)
            q = []
            count = 0
            ex = arr[i][j]
            bfs(i, j)
            continue
        if arr[i][j] != 0 and (arr[i][j+1] == 0 or arr[i+1][j] == 0 or arr[i][j-1] == 0 or arr[i-1][j] == 0):
            visit_2 = deepcopy(visit)
            q = []
            count = 0
            ex = arr[i][j]
            bfs(i, j)
print(ans)