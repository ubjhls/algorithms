for i in range(10):
    testcase = int(input())

    mag = [list(map(int, input().split())) for _ in range(testcase)]
    count = 0

    for j in range(testcase):
        for k in range(testcase-1):
            if mag[k][j] == 1 and mag[k+1][j] == 2:
                count += 1
                continue
            elif mag[k][j] == 1:
                mag[k+1][j] = mag[k][j]
                mag[k][j] = 0
            else:
                continue
    print('#{} {}'.format(i+1, count))