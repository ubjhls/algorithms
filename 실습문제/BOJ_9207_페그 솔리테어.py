def back(x, y):



n = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for t in range(n):
    peg = [input() for _ in range(5)]
    for i in range(5):
        for j in range(9):
            if peg[i][j]== 'o':
                back(i,j)