
def backtrack(k, s):        # k : 트리의 높이, 문항번호, s : 지금까지 점수 합
    if visit[k][s]: return
    visit[k][s] = 1
    if k == N:
        global cnt
        cnt += 1
    else:
        backtrack(k + 1, s)             # k번 문제 틀림
        backtrack(k + 1, s + scores[k])     # k번 문제 맞음

T = int(input())
for i in range(1, T+1):
    scores = [1] * 10
    N = len(scores)
    visit = [[0] * (N * 100 + 1) for _ in range(N + 1)]
    cnt = 0
    backtrack(0,0)
    print('#{} {}'.format(i, cnt))