from itertools import combinations

def cal(A, B):
    tmp_1 = 0
    tmp_2 = 0
    for i in combinations(A, 2):
        tmp_1 += cook[i[0]][i[1]] + cook[i[1]][i[0]]
    for i in combinations(B, 2):
        tmp_2 += cook[i[0]][i[1]] + cook[i[1]][i[0]]
    ans = abs(tmp_1 - tmp_2)
    return ans

N = int(input())
cook = [list(map(int, input().split())) for _ in range(N)]
tmp = []
taste = []
result = 0xffffff
for i in range(N):
    tmp.append(i)

for element in combinations(tmp, N // 2):
    taste.append(element)

for j in range(len(taste) // 2 + 1):
    A = taste[j]
    B = taste[-1 - j]
    answer = cal(A, B)
    if result > answer:
        result = answer
print(result)