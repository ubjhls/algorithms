testcase = int(input())

for i in range(testcase):
    a = int(input())
    number = map(int,input().split())
    result = []
    print('#{}'.format(i+1),end = ' ')
    for j in number:
        result.append(j)
    result = sorted(result)

    for j in range(len(result)):
        print(result[j], end = ' ')
    print('')