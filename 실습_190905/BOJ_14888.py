import itertools

def calculation(num_1, num_2, X):
    global result
    if X == '+':
        result = num_1 + num_2
    elif X == '-':
        result = num_1 - num_2
    elif X == '*':
        result = num_1 * num_2
    elif X == '/':
        if num_1 < 0:
            num_1 = -num_1
            result = -(num_1 // num_2)
        else:
            result = num_1 // num_2
    return result
n = int(input())
num = list(map(int, input().split()))
A = list(map(int, input().split()))
tmp = ''
answer = []
for i in range(A[0]):
    tmp += '+'
for i in range(A[1]):
    tmp += '-'
for i in range(A[2]):
    tmp += '*'
for i in range(A[3]):
    tmp += '/'
cal = list(itertools.permutations(tmp))
for m in range(len(cal)):
    result = num[0]
    for i in range(1, len(num)):
        num_1 = result
        num_2 = num[i]
        X = cal[m][i - 1]
        calculation(num_1, num_2, X)
    answer.append(result)
print(max(answer))
print(min(answer))