from collections import deque
def bfs(start):
    global count
    stack.append(start)
    while True:
        for i in range(len(stack)):
            num = stack.popleft()
            if not visit[num]:
                visit[num] = True
                if num == end:
                    return
                if 0 <= num + 1 <= 1000000:
                    stack.append(num + 1)
                if 0 <= num - 1 <= 1000000:
                    stack.append(num - 1)
                if 0 <= num * 2 <= 1000000:
                    stack.append(num * 2)
                if 0 <= num - 10 <= 1000000:
                    stack.append(num - 10)
        count += 1

T = int(input())
for t in range(1, T + 1):
    start, end = map(int, input().split())
    stack = deque()
    count = 0
    visit = [False] * 1000001
    bfs(start)
    print('#{} {}'.format(t, count))