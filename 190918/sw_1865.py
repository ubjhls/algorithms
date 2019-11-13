import sys; sys.stdin = open("input.txt", "r")
def DFS(start):
    global sub_result, result, final_result

    if len(sub_result) == N:
        for j, k in sub_result:
            result *= arr[j][k]
        final_result.append(result)
        result = 1
        return

    for next in range(0, N):
        for start in range(0, N):
            if not visit_1[next]:
                if not visit_2[start]:
                    sub_result.append((start, next))
                    visit_1[next] = True
                    visit_2[start] = True
                    DFS(start)
                    sub_result.remove((start, next))
                    visit_1[next] = False
                    visit_2[start] = False

T = int(input())
for i in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit_1 = [False] * N
    visit_2 = [False] * N
    sub_result = []
    final_result = []
    result = 1
    DFS(0)
    final_result = round(max(final_result) / 100**(N-1), 6)
    print('#{} {}'.format(i+1, final_result))