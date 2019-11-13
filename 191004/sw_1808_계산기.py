def check_button(n):
    cnt = 0
    while n > 0:
        if B[n % 10] == 0:
            return -1
        cnt += 1
        n = n // 10
    return cnt

def dfs(n):
    min = float("INF")
    d = 2
    while d < n // 2:
        if n % d == 0:  # N = n1 * n2
            n1 = d
            n2 = n // d
            l_n1 = check_button(n1)
            if l_n1 == -1:
                d += 1
                continue
            l_n2 = check_button(n2)
            if l_n2 == -1:
                l_n2 = dfs(n2)
                if l_n2 == float("INF"):
                    d += 1
                    continue
            if min > (l_n1 + 1 + l_n2):
                min = l_n1 + 1 + l_n2
        d += 1
    return min

T = int(input())
for t in range(1, T + 1):
    B = list(map(int, input().split()))
    N = int(input())
    len = check_button(N)
    if len != -1:
        result = len + 1
    else:
        result = dfs(N)
        if result == float("INF"):
            result = -1
        else:
            result += 1
    print("#{} {}".format(t, result))