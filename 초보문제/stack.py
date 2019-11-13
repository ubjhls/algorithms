def DFS(v):
    visit[v] = True; print(v, end=' ')
    for w in G[v]:
        if not visit[w]:    # v의 방문하지 않은 인접정점 w에 찾아서
            DFS(w)

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)