from itertools import combinations
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = []
    result = 0xffffff
    for i in range(N):
        num.append(i)
    for i in range(len(num)):
        for j in range(len(num)):
            if i == j:
                continue
            for k in range(len(num)):
                if i == k or j == k:
                    continue
                for m in range(len(num)):
                    if i == m or j == m or k == m:
                        continue
                    a = abs((arr[i][j] + arr[j][i]) - (arr[k][m] + arr[m][k]))
                    if result > a:
                        result = a
    print('#{} {}'.format(t, result))