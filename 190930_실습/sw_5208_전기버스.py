def back(index, battery, result):
    global ans
    if ans < result:
        return
    for j in range(1, battery + 1):
        index = index + j
        if index >= bus[0]:
            ans = result
            return
        back(index, bus[index], result + 1)
        index -= j


T = int(input())
for i in range(1, T + 1):
    ans = 100
    bus = list(map(int, input().split()))
    result = 0
    battery = bus[1]
    back(1, battery, result)
    print('#{} {}'.format(i, ans))