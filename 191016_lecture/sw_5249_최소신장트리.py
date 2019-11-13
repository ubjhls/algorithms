T = int(input())
for t in range(1, T + 1):
    v, e = map(int, input().split())
    tree = [tuple(map(int, input().split())) for _ in range(e)]
    result = [0]
    tmp  = [0]
    while True:
        a = tmp.pop()
        for i in range(len(tree)):
            if a == tree[0]:
                tmp.append(tree[1])
