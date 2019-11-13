def back(value):
    global result
    if result <= value - b:
        return
    if value - b > 0:
        if result > value - b:
            result = value - b
    for j in range(len(height)):
        if not visit[j]:
            visit[j] = True
            back(value + height[j])
            visit[j] = False


T = int(input())
for i in range(T):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    visit = [False] * n
    result = 0xffffff
    back(0)
    print('#{} {}'.format(i + 1, result))