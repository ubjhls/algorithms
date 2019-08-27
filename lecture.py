# arr = 'ABC' ; N = len(arr)
# bits = [0] * N
#
# def subset(k, n):       # k = 현재 노드의 높이, n: 단말 노드의 높이
#     if k == n:          # 모든선택이 완료, 단말노드에 도착,
#         for i in range(N):
#             if bits[i]: print(arr[i], end = '')
#         print()
#         return
#     # 선택이 남아있다.
#     bits[k] = 1; subset(k + 1, n)    # 왼쪽
#     bits[k] = 0; subset(k + 1, n)    # 오른쪽
# subset(0, N) # 0 = 어떤선택도 하지 않았다.
#              # N = 해야할 선택의 수

# for i in range(2):
#     bits[0] = i
#     for j in range(2):
#         bits[1] = j
#         for k in range(2):
#             bits[2] = k
#             print(bits)

#------------------------------------------------------------------------
# coin = [6, 4, 1]
# choose = [0] * 100
# MIN = 0xffffff
# def coinChange(k, n):
#     if k >= MIN: return
#     if n == 0:
#         for i in range(k):
#             print(choose[i], end=' ')
#         print()
#         return
#     for c in coin:
#         if c > n: continue
#         choose[k] = c
#         coinChange(k + 1, n - c)
# coinChange(0,8)

#------------------------------------------------------------------------
arr = 'ABC'; N = len(arr)
order = [0] * N

# def perm(k, n, used):
#     if k == n:
#         for i in range(n):
#             print(arr[order[i]], end = ' ')
#         print()
#         return
#     for i in range(n):
#         if used & (1 <<i): continue
#         order[k] = i
#         perm(k + 1, n, used | (1 << i))
# perm(0, N, 0)

arr = [6, 4, 2, 5, 1, 9, 2, 11, 8, 7]

def getMin(lo, hi):             # lo : 범위의 시작, hi : 범위끝
    if lo == hi:
        return arr[lo]
    mid = (lo + hi) >> 1

    return min(getMin(lo, mid), getMin(mid + 1, hi))

    pass

print(getMin(0, len(arr) - 1))