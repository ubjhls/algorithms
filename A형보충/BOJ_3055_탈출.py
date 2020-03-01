from collections import deque

n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물 차는 시간 먼저 구하기 (토마토 문제랑 동일)
# 구하는 김에 고슴도치랑 비버의굴 위치도 구하기
water = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            q.append((i, j))
            water[i][j] = 0
        elif a[i][j] == 'S':
            go_i, go_j = i, j
        elif a[i][j] == 'D':
            d_i, d_j = i, j
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
        	#못가는 경우를 조건 걸어서 거르는 방식으로
            if a[nx][ny] in 'XD':
            	continue
            if water[nx][ny] != -1:
            	continue
            q.append((nx, ny))
            water[nx][ny] = water[x][y] + 1


# 고슴도치 이동 시작!
dist = [[-1] * m for _ in range(n)]
q = deque()
q.append((go_i, go_j))
dist[go_i][go_j] = 0

while q:
    x, y = q.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 돌이거나, 물이 이미 찬 곳이면 건너뛴다.
            if dist[nx][ny] != -1:
            	continue
            if a[nx][ny] == 'X':
            	continue
            if (dist[x][y] + 1) >= water[nx][ny] and water[nx][ny] != -1:
            	continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

#출력
if dist[d_i][d_j] == -1:
    print("KAKTUS")
else:
    print(dist[d_i][d_j])