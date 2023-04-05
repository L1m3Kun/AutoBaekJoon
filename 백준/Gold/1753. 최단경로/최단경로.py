import sys
# from collections import deque
import heapq
input = sys.stdin.readline

def dijkstra(s, V):
    que = []
    heapq.heappush(que, (0, s))
    Dist[s] = 0
    while que:
        t, i = heapq.heappop(que)
        if t > Dist[i]:
            continue
        for k, j in arr[i]:
            next_w = t + k
            if Dist[j] > next_w:
                heapq.heappush(que,(next_w, j))
                Dist[j] = next_w
    return




V, E = map(int, input().split())
s = int(input())
INF = 1000000
arr = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w,v))

Dist = [INF] * (V+1)
dijkstra(s, V)
for i in range(1,V+1):
    if Dist[i] == INF:
        print("INF")
    else:
        print(Dist[i])

