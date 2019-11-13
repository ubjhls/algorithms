def dfs(x, k):
    global result
    if k == 2: return

    for v in G[x]:
        if v == 1: continue
        result.add(v)
        dfs(v, k + 1)

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    result = set()

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    dfs(1, 0)
    print('#{} {}'.format(t, len(result)))