def divide(num):
    global count
    tmp = []
    middle = len(num) // 2
    if num[middle] == j:
        count += 1
        return
    if len(num) == 1:
        if num[0] == j:
            count += 1
            return
        else:
            return
    if j > num[middle]:
        for k in range(middle, len(num)):
            tmp.append(num[k])
        divide(tmp)
    else:
        for k in range(0, middle):
            tmp.append(num[k])
        divide(tmp)

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for j in A:
        divide(B)
    print('#{} {}'.format(i + 1, count))