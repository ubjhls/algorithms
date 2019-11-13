def find_max(L):
    Max = L[0] ** 2
    for i in range(M - 1):
        for j in range(i + 1, M):
            k = j
            Sum = L[i]
            sub_max = L[i] ** 2
            while k < M:
                if Sum + L[k] <= C:
                    Sum += L[k]
                    sub_max += L[k] ** 2
                k += 1
            Max = max(Max, sub_max)
    return Max

T = int(input())
for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_arr = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N - M + 1):
            select = sorted([arr[i][j + m] for m in range(M)], reverse=True)
            max_arr[i][j] = find_max(select)
    sub_arr = sum(max_arr, [])
    for i in range(N ** 2 - M):
        ans = max(ans, sub_arr[i] + max(sub_arr[i + M:]))
    print('#{} {}'.format(t, ans))