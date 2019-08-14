testcase = int(input())
number = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
for i in range(testcase):
    print('#{}'.format(i+1))
    test_num = list(map(str, input().split()))
    test_result = list(map(str, input().split()))
    for k in range(10):
        for j in range(test_result.count(number[k])):
            print(number[k],end=' ')