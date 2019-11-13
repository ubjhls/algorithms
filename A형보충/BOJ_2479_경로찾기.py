def bfs(start):
    q.append(start)
    visit[start] = True
    while q:
        start = q.pop(0)
        for i in range(n):
            count = 0
            for j in range(len(arr[start])):
                if arr[start][[j]] == arr[i][j]:
                    count += 1


n, k = map(int, input().split())
arr = [input() for _ in range(n)]
start, end = map(int, input().split())
start = start - 1
end = end - 1
visit = [False] * n + 1
q = []
bfs(start)