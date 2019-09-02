num = int(input())
tmp = ''
for i in range(num):
    result = i
    for j in str(i):
        tmp = ''
        tmp += j
        result += int(tmp)
    if result == num:
        break
    elif i == num-1:
        i = 0
print(i)