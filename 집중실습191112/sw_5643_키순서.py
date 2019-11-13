import collections

def bfs(v, adj):
    q = collections.deque()
    rtn = 0
    visited[v] = True
    q.append(v)

    while q:
        v = q.popleft()
        for nv in adj[v]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
                rtn += 1
    return rtn

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    M = int(input())
    shorter_adj = [[] for _ in range(N+1)]
    higher_adj = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        shorter_adj[a].append(b)
        higher_adj[b].append(a)

    ans = 0
    for n in range(1, N+1):
        visited = [False]*(N+1)
        r = bfs(n, shorter_adj) + bfs(n, higher_adj) + 1
        if r == N: ans += 1
    print('#{} {}'.format(t,ans))