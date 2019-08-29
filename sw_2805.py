T = int(input())

for i in range(T):
    case = int(input())
    farm = [list(map(int, input())) for _ in range(case)]
    R = case // 2
    count = 0
    result = 0
    for j in range(R+1):
        for m in range(R - j, R + 1 + j):
            result += farm[j][m]
    for j in range(case - 1, case - R - 1, -1):
        for m in range(j - R, case - R + count):
            result += farm[j][m]
        count += 1

    print('#{} {}'.format(i+1, result))