T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input())) for _ in range(H)]

