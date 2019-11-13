testcase = int(input())
for i in range(testcase):
    str_1 = input()
    str_2 = input()
    result = []
    for j in range(len(str_1)):
        result.append(str_2.count(str_1[j]))
    print('#{} {}'.format(i+1,max(result)))
