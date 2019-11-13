def quick(num):
    if len(num) <= 1:
        return num
    pivot = num[0]
    lo, middle, hi = [], [], []
    for j in num:
        if j < pivot:
            lo.append(j)
        elif j > pivot:
            hi.append(j)
        else:
            middle.append(j)
    return quick(lo)+middle+quick(hi)

T = int(input())
for i in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    result = quick(num)
    print('#{} {}'.format(i + 1, result[n // 2]))