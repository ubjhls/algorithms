def back(v, a):
    global max, min
    if v == num:
        if max < a:
            max = a
        if min > a:
            min = a
        return
    else:
        if cal[0] != 0:
            cal[0] -= 1
            back(v + 1, a + number[v])
            cal[0] += 1

        if cal[1] != 0:
            cal[1] -= 1
            back(v + 1, a - number[v])
            cal[1] += 1

        if cal[2] != 0:
            cal[2] -= 1
            back(v + 1, a * number[v])
            cal[2] += 1

        if cal[3] != 0:
            cal[3] -= 1
            back(v + 1, int(a / number[v]))
            cal[3] += 1


T = int(input())
for t in range(1, T + 1):
    num = int(input())
    cal = list(map(int, input().split()))
    number = list(map(int, input().split()))
    max = -0xffffff
    min = 0xfffff
    back(1, number[0])
    print('#{} {}'.format(t, max - min))