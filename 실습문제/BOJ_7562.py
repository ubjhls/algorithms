def bfs(x, y):
    global count
    if start_x == end_x and start_y== end_y:
        return
    count += 1
    visit[x][y] = True
    q.append((x,y))
    while q:
        for k in range(len(q)):
            x, y = q.pop(0)
            for j in range(8):
                nx, ny = x + dx[j], y + dy[j]
                if nx < 0 or ny < 0 or nx >= l or ny >= l:
                    continue
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    if nx == end_x and ny == end_y:
                        return
                    q.append((nx, ny))
        count += 1

T = int(input())
for i in range(T):
    l = int(input())
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    visit = [[False] * l for _ in range(l)]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    q = []
    count = 0
    bfs(start_x, start_y)
    print(count)