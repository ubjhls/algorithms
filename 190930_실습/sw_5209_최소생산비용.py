def back(value, y):
    global result
    if result < value:
        return
    if y == num:
        if result > value:
            result = value
        return
    for j in range(num):
        if not visit[j]:
            visit[j] = True
            back(value + arr[y][j], y + 1)
            visit[j] = False


T = int(input())
for i in range(T):
    num = int(input())
    result = 10000
    arr = [list(map(int, input().split())) for _ in range(num)]
    visit = [False] * num
    back(0, 0)
    print('#{} {}'.format(i+1, result))