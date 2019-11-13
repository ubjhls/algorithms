def dfs(num):
    global count
    q.append(num)
    while q:
        a = q.pop()
        if not visit[a]:
            visit[a] = True
            for k in range(len(arr[a])):
                q.append(arr[a][k])
                count += 1

T = int(input())
for t in range(1, T + 1):
    count = 1
    arr = [[] for _ in range(1000)]
    visit = [False] * 1000
    q = []
    e, n = map(int, input().split())
    l = list(map(int, input().split()))
    for j in range(0,  2 * e, 2):
        arr[l[j]].append(l[j + 1])
    dfs(n)
    print('#{} {}'.format(t, count))