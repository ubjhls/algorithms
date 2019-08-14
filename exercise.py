testcase = int(input())
for i in range(testcase):
    count = 0
    test = list(str(input()))
    for j in range(len(test)//2):
        if test[j] == test[-1-j]:
            count += 1
            if len(test)//2 == count:
                print('#{} {}'.format(i+1,1))
                break
    else:
            print(('#{} {}'.format(i+1,0)))