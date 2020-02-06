from copy import deepcopy
for T in range(1, int(input())+1):
    tmp, n = input().split()
    n = int(n)
    numbers = [tmp[i] for i in range(len(tmp))]
    dp = [[] for _ in range(n+1)]
    dp[0] = [numbers]
    for j in range(1, n+1):
        for i in range(len(dp[j-1])):
            for k in range(len(tmp)):
                for l in range(k+1, len(tmp)):
                    tmp = deepcopy(dp[j - 1][i])
                    tmp[k], tmp[l] = tmp[l], tmp[k]
                    if tmp not in dp[j]:
                        dp[j].append(tmp)
    result = 0
    for i in range(len(dp[n])):
        val = int(''.join(dp[n][i]))
        result = max(val, result)
    print('#{} {}'.format(T, result))