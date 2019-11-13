def bfs(a):
    visit[a] = True
    t.append(a)
    count = 0
    while t:
        tmp = t.pop(0)
        for i in Q[tmp]:
            if not visit[i]:
                visit[i] = True
                t.append(i)
                count += 1
    return count

com = int(input())
num = int(input())
t = []
Q = [[] for _ in range(com + 1)]
visit = [False for _ in range(com + 1)]
for i in range(num):
    N, M = map(int,input().split())
    Q[N].append(M)
    Q[M].append(N)

print(bfs(1))