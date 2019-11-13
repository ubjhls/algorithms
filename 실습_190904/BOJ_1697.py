import sys
sys.setrecursionlimit(100001)


def bfs(v):
    visited = [False] * 100001
    q = [v]
    count = 0
    result = False
    while q:
        for i in range(len(q)):
            v = q.pop(0)
            if not(visited[v]):
                visited[v] = True
                if v == end:
                    result = True
                    break
                if v - 1 >= 0:
                    q.append(v - 1)
                if v + 1 <= 100000:
                    q.append(v + 1)
                if v * 2 <= 100000:
                    q.append(v * 2)
        if result:
            print(count)
            break
        count += 1

start, end = map(int,input().split())
bfs(start)
