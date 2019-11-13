from collections import deque
def bfs(v):
    q = deque()
    visited = [False]*(n+1)
    q.append(v)
    visited[v] = True
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            v = q.popleft()
            if v == end:
                return level - 1
            for e in adj[v]:
                if not(visited[e]):
                    visited[e] = True
                    q.append(e)
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

print(bfs(start))