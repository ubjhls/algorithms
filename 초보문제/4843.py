testcase = int(input())

for i in range(testcase):
    count = int(input())
    result=[]
    numbers = list(map(int, input().split()))
    print('#{}'.format(i+1),end = ' ')
    k= 0
    while k < 5:
        k += 1
        result.append(max(numbers))
        numbers.remove(max(numbers))
        result.append(min(numbers))
        numbers.remove(min(numbers))

    for j in range(len(result)):
        real_result=''
        real_result += str(result[j])
        print(real_result,end = ' ')
        if j==len(result)-1:
            print('')