L, C = map(int,input().split())
O = 'bcdfghjklmnpqrstvwxyz'
word = list(map(str,input().split()))
n = len(word)
result = []
password = ''
for i in range(1 << n):
    password = ''
    for j in range(n):
        tmp = i & (1 << j)
        if tmp:
            password += word[j]
    if len(password) == L:
        result.append(sorted(password))
answer = sorted(result)


for i in range(len(answer)):
    count = 0
    if 'a' in answer[i] or 'e' in answer[i] or 'i' in answer[i] or 'o' in answer[i] or 'u' in answer[i]:
        for j in range(len(answer[i])):
            if answer[i][j] in O:
                count += 1
            if count == 2:
                print(''.join(answer[i]))
                break
    else:
        continue

#-----------------------------------------------------

pwd = []
alpha = ('a', 'e', 'i', 'o', 'u')
def backtrack(k, mo, ja):
    if len(pwd) == L:
        print(pwd)
        return
    if k == C: return

    pwd.append(arr[k])
    a = b = 0
    if arr[k] in alpha: a = 1
    else: b = 1
    backtrack(k + 1, mo + a, ja + b)    # k번쨰 요소를 포함하는 경우
    pwd.pop()
    backtrack(k + 1, mo, ja)    # k번째 요소를 포함하지 않는 경우
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

backtrack(0,0,0)

#---------------------------------------------------------------
ar = 'ABCDE'; N = len(ar)
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1 ,N):
            print(arr[i], arr[j],arr[k])