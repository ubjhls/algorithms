n = int(input())
d = [[0]*10 for _ in range(n+1)]
ans, mod = 0, 1000000000

def solve():
    for i in range(1, 10):
        d[1][i] = 1
    for i in range(2, n+1):
        for j in range(0, 10):
            if j > 0:
                d[i][j] += d[i-1][j-1]

            if j < 9:
                d[i][j] += d[i-1][j+1]
            d[i][j] %= mod

solve()
print(sum(d[n]) % mod)
