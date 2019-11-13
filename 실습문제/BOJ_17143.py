R, C, M = map(int,input().split())
arr = [[0] * (C) for _ in range(R)]
dx = [0,0, 0, 1, -1]
dy = [0,-1, 1, 0, 0]
result = 0
for i in range(M):
    tmp = list(map(int,input().split()))
    arr[tmp[0]-1][tmp[1]-1] = (tmp[2],tmp[3],tmp[4])

for i in range(C):
    for j in range(R):
        if arr[j][i] != 0:
            result += arr[j][i][2]
            arr[j][i] = 0
            break
    for j in range(R):
        for k in range(C):
            if arr[j][k] != 0:
                for m in range(arr[j][k][0]):
                    if arr[j][k][1] == 1:
                        if j == arr[j][k]:
                            nj, nk = j+dx[1], j+dy[1]
                            arr[nj][nk] = arr[j][k]
                            arr[j][k] = 0

