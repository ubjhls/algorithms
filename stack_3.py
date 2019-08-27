for w in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break
    dir = 0             # 0: 위, 1: 왼쪽, 2: 오른쪽
    while x:
        if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
            y, dir = y - 1, 1
        elif dir != 1 and y + 1 < 100 and arr[x][y+1]:
            y, dir = y + 1, 2
        else:
            x, dir = x - 1, 0
    print(y)