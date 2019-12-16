from copy import deepcopy
def back(x, y, count):
    pass

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr2 = deepcopy(arr)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            back(i, j)