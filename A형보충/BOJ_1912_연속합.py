n = int(input())
number = list(map(int, input().split()))
dp = []
dp.append(number[0])

for i in range(1, len(number)):
    if dp[i - 1] < 0:
        dp.append(number[i])
    else:
        dp.append(dp[i-1] + number[i])

print(max(dp))