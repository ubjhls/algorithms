from itertools import combinations
from copy import deepcopy
def dfs(x):
    for o in range(len())


n = int(input())
people = list(map(int, input().split()))
po = [[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(1, len(tmp)):
        po[i].append(tmp[j])
vote = [i for i in range(n)]
for i in range(1, n // 2 + 1):
    for j in combinations(vote, i):
        A = j
        vote_tmp = deepcopy(vote)
        for k in A:
            vote_tmp.remove(k)
        B = vote_tmp
        dfs(A[0])