def cal(x,y,z):
    result = 0
    if z == '+':
        result = int(x) + int(y)
    elif z == '-':
        result = int(x) - int(y)
    elif z == '*':
        result = int(x) * int(y)
    elif z == '/':
        result = int(x) // int(y)
    return result


testcase = int(input())

for i in range(testcase):
    forth = input().split()
    stack = []
    tmp_1 = 0
    tmp_2 = 0
    for j in forth:
        if j == '+' or j == '-' or j == '*' or j == '/' or j == '.':
            if j == '.':
                break
            elif len(stack) == 1:
                stack.pop()
                stack.append('error')
                break
            elif len(stack) == 0:
                stack.append('error')
                break
            else:
                tmp_1 = stack.pop()
                tmp_2 = stack.pop()
                stack.append(cal(tmp_1, tmp_2, j))
        else:
            stack.append(j)
    print('#{} {}'.format(i+1, stack[0]))