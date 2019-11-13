# scores = [1] * 10
# N = len(scores)
# visit = [[0] * (N * 100 + 1) for _ in range(N + 1)]
# cnt = 0
#
# Q = []
# Q.append(0)
# for k in range(len(scores)):
#     for i in range(len(Q)):
#         t = Q[i] + scores[k]
#         if visit[i][t] == 0:
#             Q.append(t)
#             visit[i][t] = 1
#
# print(len(Q))
#----------------------------------
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     visit = [0] * 100001
#     visit[0] = 1
#     for s in scores:
#         for i in range(10000, -1, -1):
#             if visit[i]:
#                 visit[i + s] = 1
#     print('#{} {}'.format(tc, visit.count(1)))
#
#--------------------------------------
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    A = set()
    A.add(0)
    for s in scores:
        B = set()
        for a in A:
            B.add(s + a)
        A = A|B
    print('#{} {}'.format(tc, len(A)))

#----------------------------------------

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