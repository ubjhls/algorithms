def Dijkstra(G,K,z):
    for i in range(len(K)):
        heappush(q,(0,K[i]))
        G[K[i]]=0
    while q:
        t,x=heappop(q)
        if G[x]!=t:continue
        for nx,nt in D[x]:
            if nt+t<=z and G[nx]>nt+t:
                G[nx]=nt+t;heappush(q,(nt+t,nx))
from heapq import *
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[[] for _ in range(n+1)]
S=[float('inf')]*(n+1)
M=[float('inf')]*(n+1)
q=[]
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
    D[b].append((a,c))
a,b=map(int,input().split())
Mac=[*map(int,input().split())]
Dijkstra(M,Mac,b)
c,d=map(int,input().split())
Star=[*map(int,input().split())]
Dijkstra(S,Star,d)
for i in range(n+1):
    if M[i]==0 or S[i]==0: M[i]=float('inf')
    else: M[i] += S[i]
k=min(M)
print([k,-1][k==float('inf')])