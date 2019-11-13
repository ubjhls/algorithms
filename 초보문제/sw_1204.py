T = int(input())

for i in range(T):
    num = int(input())
    grade = list(map(int, input().split()))
    result = []
    for j in range(101):
        tmp = grade.count(j)
        result.append(tmp)
        if max(result) == tmp:
            binsu = j
    print('#{} {}'.format(num, binsu))
