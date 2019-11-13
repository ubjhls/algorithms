def bfs():
    global count, q
    while q:
        if len(tmp) == num:
            return
        for m in range(len(q)):
            a = q.pop(0)
            for i in range(len(Q[a])):
                if Q[a][i] not in tmp:
                    q.append(Q[a][i])
                    tmp.append(Q[a][i])
        count += 1

num = int(input())
people = []
Q = [[] for _ in range(num + 1)]
result = []
ans = []
while True:
    n, m = map(int, input().split())
    if n != -1:
        Q[n].append(m)
        Q[m].append(n)
    else:
        break
for j in range(1, num + 1):
    q = []
    tmp = []
    count = 0
    q.append(j)
    tmp.append(j)
    bfs()
    result.append((count, j))
min_value = min(result)[0]
for w in range(len(result)):
    if result[w][0] == min_value:
        ans.append(result[w][1])
print(min_value, end = ' ')
print(len(ans))
print(*ans)