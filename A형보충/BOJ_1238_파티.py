import heapq

def dijkstra(v):
    q = []
    heapq.heappush(q, [0, v])
    while q:
        v = heapq.heappop(q)
        for tmp in arr[v[1]]:
            cal = tmp[1] + v[0]
            if cal < answer[tmp[0]]:
                answer[tmp[0]] = cal
                heapq.heappush(q, [answer[tmp[0]], tmp[0]])


N, M, X = map(int, input().split())
arr = [[] for _ in range(M + 1)]
result = []
for i in range(1, M + 1):
    s, e, l = map(int, input().split())
    arr[s].append([e, l])

for i in range(1, N + 1):
    if i == X:
        continue
    answer = [0xffffff] * (N + 1)
    dijkstra(i)
    val_1 = answer[X]
    answer = [0xffffff] * (N + 1)
    dijkstra(X)
    val_2 = answer[i]
    result.append(val_1+val_2)

print(max(result))

