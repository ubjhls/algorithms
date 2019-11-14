def bfs():




def start():
    for i in range(200, 400, 1):
        for j in range(200, 400, 1):
            for k in range(len(N)):
                for l in range(len(M)):
                    arr_1[i+k][j+l] = cell[k][l]
                    arr_2[i+k][j+l] = 2 * cell[k][k]
                    visit[i+k][j+l] = True
            return


T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(N)]
    arr_1 = [[0] * 400 for _ in range(400)]
    arr_2 = [[0] * 400 for _ in range(400)]
    visit = [[False] * 400 for _ in range(400)]
    dx = [0, 0, 1, -1]
    dy = [1, -1 ,0 ,0]
    n = len(arr_1) // 2
    start()
    for i in range(400):
        for j in range(400):
            if arr_1[i][j]:


