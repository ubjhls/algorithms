import heapq

def bfs():
    while q:
        val, x, y = heapq.heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cal = val + arr[nx][ny]
            if dp[nx][ny] > cal:
                dp[nx][ny] = cal
                heapq.heappush(q, [dp[nx][ny], nx, ny])

count = 0
while True:
    count += 1
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    dp = [[0xfffff] * n for _ in range(n)]
    dp[0][0] = arr[0][0]
    heapq.heappush(q, [arr[0][0], 0, 0])
    bfs()
    print('{} {}: {}'.format('Problem', count, dp[n-1][n-1]))
