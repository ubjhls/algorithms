# N = 10
# Q = [0] * 10
# front = rear = -1
#
# def enqueue(item):
#     global rear
#     # full 상태 체크
#     if front ==  (rear + 1) % N:
#         return
#     rear = (rear + 1) % N
#     Q[rear] = item
#
# def dequeue():
#     global front
#     # empty 상태 체크
#     if front == rear: return
#     front = (front + 1) % N
#     return Q[front]
#
# Q = []
# Q.append(1)
# while len(Q) > 0:
#     Q.pop(0)
#
# from queue import Queue, PriorityQueue
# import collections
# Q = collections.deque()
#
# -------------------------------------------------

# from queue import PriorityQueue
#
# arr = [(3,5),(3,4),(8,9),(1,4),(2,6)]
# PQ = PriorityQueue()
# for val in arr:
#     PQ.put(val)
#
# while not PQ.empty():
#     print(PQ.get())

# -------------------------------
def BFS(s):    # s= 시작점
    # 큐를 생선, 방문표시
    # 시작점을 방문하고 큐에 삽입
    # 빈큐가 아닐동안
    # 큐에서 하나를 ㄲ내온다. v
    # v의 방문하지 않은 모든 인접정점을 찾아서
    # 차례로 방문하고 큐에 삽입
    Q = []
    visit = [False] * (V + 1)
    visit[s] =True; print(s)
    D[s] , D[p] = 0, p
    Q.append(s)
    while Q:
        v=Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                visit[w] = True; print(w)
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)
import sys
sys.stdin = open("BFS_input.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)