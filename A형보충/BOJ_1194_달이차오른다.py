from collections import deque

def bfs():
    global answer, count, q
    visit = [[False] * M for _ in range(N)]
    while q:
        for w in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if not visit[nx][ny] and arr[nx][ny] !='#':
                    if arr[nx][ny] == '1':
                        answer = 1
                        count += 1
                        return
                    if arr[nx][ny] != '.':
                        if 97 <= ord(arr[nx][ny]) < 123:
                            key.append(chr(ord(arr[nx][ny]) - 32))
                            arr[nx][ny] = '.'
                            q = deque()
                            q.append((nx, ny))
                            count += 1
                            return
                        else:
                            if arr[nx][ny] in key:
                                arr[nx][ny] = '.'
                                q.append((nx, ny))
                                visit[nx][ny] = True
                                continue
                            else:
                                continue
                    visit[nx][ny] = True
                    q.append((nx, ny))
        count += 1
    answer = -1
def init():
    global answer, count
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                arr[i][j] = '.'
                q.append((i, j))
                while True:
                    bfs()
                    if answer == 1:
                        return
                    elif answer == -1:
                        count = -1
                        return

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
key = []
count = 0
answer = 0
init()
print(count)
