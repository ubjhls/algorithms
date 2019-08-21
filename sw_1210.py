for w in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    tmp = []
    p = 0
    for j in range(100):
        if arr[99][j] == 2:
            tmp.append(j)
            break

    for i in range(99, 0, -1):
        p = 0
        q = 0
        for k in range(99):
            if arr[i][tmp[0] - 1] == 1:
                if q == 0:
                    tmp.append(tmp[0] - 1)
                    tmp.pop(0)
                    p += 1
                else:
                    break
            if arr[i][tmp[0] + 1] == 1:
                if p == 0:
                    tmp.append(tmp[0] + 1)
                    tmp.pop(0)
                    q += 1
                else:
                    break
            else:
                break
    print('#{} {}'.format(w+1, tmp[0]))