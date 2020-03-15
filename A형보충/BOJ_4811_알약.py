while True:
    n = int(input())
    if n == 0:
        break
    r = 1
    for n in range(2*n, n, -1):
        r *= n
    for n in range(1, n+1):
        r //= n
    print(r)