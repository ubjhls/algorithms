import sys

sys.stdin = open("1267_input.txt", "r")
for t in range(10):
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    g = [[] for i in range(v + 1)]
    visit = [0] * (v+1)
    for k in range(0, len(data), 2):
        g[data[k]].append(data[k + 1])
        visit[data[k + 1]] += 1

    result = ''
    for i in range(1, v + 1):
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            if visit[node] > 0:
                visit[node] -= 1
            elif visit[node] == 0:
                visit[node] = 'X'
                result += str(node) + ' '
                stack.extend(g[node])
    print('#{} {}'.format(t + 1, result))