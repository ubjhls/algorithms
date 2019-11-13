T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    tmp = []
    length = []
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                tmp.append((i, j))
    for sec in tmp:
        x, y = sec
        for ex in tmp:
            x_tmp, y_tmp = ex
            result.append(abs(x - x_tmp) + abs(y - y_tmp))
            result = sorted(result)
    print(result)