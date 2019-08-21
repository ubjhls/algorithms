test = int(input())

for i in range(test):
    stack = []
    word = input()
    for j in word:
        if '(' or '{' or '[' == j:
            stack.append(j)
        elif ')' or '}' or']' == j:
            if '(' or '{' or '[' in stack:
                stack.pop(0)
            else:
                print(0)
                break
    if len(stack) == 0:
        print(1)