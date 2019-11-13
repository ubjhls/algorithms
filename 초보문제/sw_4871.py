import sys

sys.stdin = open("4871_input.txt", "r")

def DFS(v):
    global result
    visit[v] = True
    for w in range(V):
        if G[v][w] and not visit[w]:
            if w == load_2:
                result = 1
                return
            DFS(w)

# ----------------------------------------------
T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    G = [[False]*(V+1) for _ in range(V + 1)]
    visit = [False] * (V+1)

    for j in range(E):
        u, v = map(int, input().split())
        G[u][v] = True
    load_1, load_2 = map(int, input().split())
    result = 0
    DFS(load_1)
    print(result)