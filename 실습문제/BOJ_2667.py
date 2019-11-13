import sys; sys.setrecursionlimit(10000)
def dfs(x, y):
    global count
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or nx >= M or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] == '1' and not visit[nx][ny]:
            visit[nx][ny] = True
            count += 1
            dfs(nx, ny)

M = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = [input() for _ in range(M)]
visit = [[False] * (M + 1) for _ in range(M + 1)]
result = []
answer = []
for i in range(M):
    for j in range(M):
        if arr[i][j] == '1' and not visit[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

for i in range(len(result)):
    if result[i] > 1:
        answer.append(result[i])
answer = sorted(answer)
print(len(answer))
for i in range(len(answer)):
    print(answer[i])