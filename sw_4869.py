T = int(input())

for i in range(T):
    num = int(input())
    count = 0
    for j in range(0, (num//10) + 1):
        for k in range(0, (num//10) + 1):
            if 10*j + 20*k == num:
                count += 1
    for j in range(0, 3):
        for k in range(0, 3):
            if 10*j + 20*k == 20:
                count += 1
    print(count)