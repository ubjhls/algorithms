T = int(input())

for i in range(T):
    charge = list(map(int, input().split()))
    a = charge[0] * charge[4]
    if charge[2] > charge[4]:
        b = charge[1]
    else:
        b = charge[1] + (charge[4] - charge[2]) * charge[3]
    print('#{} {}'.format(i+1, min(a,b)))