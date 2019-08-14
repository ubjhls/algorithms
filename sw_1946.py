testcase = int(input())
test = int(input())
count = 0
for j in range(test):
    test_input = list(map(str, input().split()))
    for i in range(int(test_input[1])):
        if count == 10:
            print('\n')
        else:
            print(test_input[0],end='')
            count += 1
