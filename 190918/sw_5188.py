import  sys ; sys.stdin = open("5188.txt", "r")

def IsSafe(y,x):
    return 0<=y<N and 0<=x<N

def DFS(y,x):
    global sub_result, result

    if result < sub_result:
        return

    if y == N-1 and x == N-1:
        result = sub_result
        return

    for dir in range(2):
        New_Y = y + dy[dir]
        New_X = x + dx[dir]
        if IsSafe(New_Y, New_X) and (New_Y, New_X) not in visited:
            visited.append((New_Y, New_X))
            sub_result += Data[New_Y][New_X]
            DFS(New_Y, New_X)
            visited.remove((New_Y, New_X))
            sub_result -= Data[New_Y][New_X]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]

    visited = []

    dy = [0, 1]
    dx = [1, 0]

    sub_result, result = Data[0][0], 1000
    DFS(0,0)
    print('#{} {}'.format(tc, result))