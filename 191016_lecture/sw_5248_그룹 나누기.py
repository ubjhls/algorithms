def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [num for num in range(N + 1)]   # 1~N
    ans = N
    for i in range(0, M * 2, 2):
        u, v = arr[i], arr[i+1]
        a = find_set(u); b = find_set(v)
        if a != b:
            p[b] = a
            ans -= 1
    print('#{} {}'.format(tc, ans))