from collections import deque
def bfs(s):
    D = [0xffffff] * (V + 1)        # D[] 초기값 설정
    Q = deque()
    Q.append(s); D[s] = 0
    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:         # u -----> v
                D[v] += D[u] + w
                Q.append(v)

V, E = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

pi = [0] * V
key = [0xffffff] * V
visit = [False] * V     #트리에 포함된 정점과 아닌 정점을 구분

key[0] = 0
cnt = V
while cnt:      # 모든 정점을 선택할때 까지
    # 아직 트리에 포함되지 않은 정점들 중에서  key 값이 최소인 정점을 찾는다.
    u, MIN = 0, 0xffffff
    for i in range(V):
        if not visit[i] and MIN > key[i]: u, MIN = i, key[i]
    visit[u] = True

    for v, w in G[u]:
        if not visit[v] and w < key[v]:
            key[v] = w
            pi[v] = u
    cnt -= 1