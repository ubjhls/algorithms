def dfs(x, y, d):
    arr[x][y] = 2
    if d == 0:
        if arr[x][y - 1] == 0:
            dfs(x, y-1, 3)
        elif arr[x][y - 1] == 1 or arr[x][y - 1] == 2:
            dfs(x, y, 3)
        elif arr[x][y-1] != 0 and arr[x-1][y] != 0 and arr[x][y+1] != 0 and arr[x+1][y] != 0:
            dfs(x + 1, y, 0)
        elif arr[x][y-1] != 0 and arr[x-1][y] != 0 and arr[x][y+1] != 0 and arr[x+1][y] == 1:
            return
    




N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dfs(r, c)