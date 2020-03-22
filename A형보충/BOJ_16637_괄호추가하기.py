def backtracking(i, res):
    global ans
    if i == N:
        ans = max(res, ans)
        return
    if s[i] == '+':
        backtracking(i+2, res+int(s[i+1]))
        if i == N-2:
            return
        a = int(s[i+1])
        o = s[i+2]
        b = int(s[i+3])
        if o == '+':
            backtracking(i+4, res+(a+b))
        elif o == '-':
            backtracking(i+4, res+(a-b))
        else:
            backtracking(i+4, res+(a*b))
    elif s[i] == '-':
        backtracking(i+2, res-int(s[i+1]))
        if i == N-2:
            return
        a = int(s[i+1])
        o = s[i+2]
        b = int(s[i+3])
        if o == '+':
            backtracking(i+4, res-(a+b))
        elif o == '-':
            backtracking(i+4, res-(a-b))
        else:
            backtracking(i+4, res-(a*b))
    else:
        backtracking(i+2, res*int(s[i+1]))
        if i == N-2:
            return
        a = int(s[i+1])
        o = s[i+2]
        b = int(s[i+3])
        if o == '+':
            backtracking(i+4, res*(a+b))
        elif o == '-':
            backtracking(i+4, res*(a-b))
        else:
            backtracking(i+4, res*(a*b))

N = int(input())
s = input()
ans = -1*10**10
backtracking(1, int(s[0]))
print(ans)