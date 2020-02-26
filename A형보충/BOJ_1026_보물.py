N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tmp_a = sorted(A)
tmp_b = sorted(B, reverse=True)
result = 0
for i in range(len(A)):
    result += tmp_a[i] * tmp_b[i]
print(result)