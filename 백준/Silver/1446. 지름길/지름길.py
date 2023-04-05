# 1446 지름길
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(s, V):
    # visited = [0] * (V+1)
    # visited[s] = 1
    que = deque([(0,0)])
    Dist[0] = 0
    while que:
        i, k = que.popleft()

        for j,w  in arr[i]:
            if 0<j<V+1 and Dist[j] > Dist[i]+w:
                que.append((j, w))
                Dist[j] = Dist[i]+w
                # visited[j] = 1
    return 



N, D = map(int, input().split())
INF = 100000000
arr = [[(_+1, 1)] for _ in range(D+1)]
for _ in range(N):
    s, e, w = map(int, input().split())
    if not e > D and (e-s) > w:
        arr[s].append((e, w))
Dist = [INF] * (D+1)
dijkstra(0, D)
print(Dist[D])