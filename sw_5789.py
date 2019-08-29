T = int(input())

for i in range(T):
    case = list(map(int, input().split()))
    box = [0] * case[0]
    num = [list(map(int, input().split())) for _ in range(case[1])]
    result = ''
    for j in range(case[1]):
        for k in range(num[j][0], num[j][1]+1):
            box[k-1] = j+1

    result += ' '.join(map(str, box))
    print('#{} {}'.format(i+1, result))