from collections import deque
def check(q):

    for m in range(4):
        if m >= len(q):
            break
        num, direction  = q[m]
        if direction == 1:
            if num == 1 or num == 2 or num == 3:
                if magnet[num][2] != magnet[num + 1][6]:
                    if not visit[num + 1]:
                        q.append((num + 1, -1))
                        visit[num + 1] = True

            if num == 2 or num == 3 or num == 4:
                if magnet[num][6] != magnet[num - 1][2]:
                    if not visit[num - 1]:
                        q.append((num - 1, -1))
                        visit[num - 1] = True
        else:
            if num == 1 or num == 2 or num == 3:
                if magnet[num][2] != magnet[num + 1][6]:
                    if not visit[num + 1]:
                        q.append((num + 1, 1))
                        visit[num + 1] = True

            if num == 2 or num == 3 or num == 4:
                if magnet[num][6] != magnet[num - 1][2]:
                    if not visit[num - 1]:
                        q.append((num - 1, 1))
                        visit[num - 1] = True


T = int(input())
for t in range(1, T + 1):
    k = int(input())
    magnet = [[]]
    result = 0
    q = deque()

    for j in range(4):
        magnet.append(deque(list(map(int, input().split()))))
    for i in range(k):
        num, direction = map(int, input().split())
        q.append((num, direction))
        visit = [False] * 5
        visit[num] = True
        check(q)
        while q:
            num, direction = q.popleft()

            if direction == 1:
                tmp = magnet[num].pop()
                magnet[num].appendleft(tmp)

            else:
                tmp = magnet[num].popleft()
                magnet[num].append(tmp)

    for w in range(1, 5):
        if w == 1:
            if magnet[w][0] == 1:
                result += 1
        if w == 2:
            if magnet[w][0] == 1:
                result += 2
        if w == 3:
            if magnet[w][0] == 1:
                result += 4
        if w == 4:
            if magnet[w][0] == 1:
                result += 8

    print('#{} {}'.format(t, result))
