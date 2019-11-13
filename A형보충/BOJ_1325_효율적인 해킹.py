from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
result = [(0,(0,0))]
ans = []

for i in range(m):
    x, y = map(int, input().split())
    arr[y].append(x)

for j in range(1, n + 1):
    visit = [False] * (n + 1)
    tmp = deque()
    if not visit[j]:
        tmp.append(j)
        count = 1
        while tmp:
            ex = tmp.popleft()
            visit[ex] = True
            for k in range(len(arr[ex])):
                tmp.append(arr[ex][k])
                count += 1
        if result[0][0] < count:
            result.clear()
            result.append((count,j))
        elif result[0][0] == count:
            result.append((count,j))
for k in range(len(result)):
    ans.append(result[k][1])
ans = sorted(ans)
print(*ans)