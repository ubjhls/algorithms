import copy
def back(x, y):
    bishop[x][y] = 2





n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]
for i in range(n):
    for j in range(n):
        if chess[i][j] == 1:
            bishop = copy.deepcopy(chess)
            back(i, j)