# 1238 파티
import sys, heapq
input = sys.stdin.readline


def dijkstra(X:int, graph:list, N:int) -> list:
    que = []
    heapq.heappush(que, (0, X)) 
    visited = [100001] * (N+1)
    
    visited[X] = 1
    while que:
        cost, now = heapq.heappop(que)
        
        for i in range(1, N+1):
            if visited[i] > cost + graph[now][i]:
                visited[i] = cost + graph[now][i]
                heapq.heappush(que, (cost+graph[now][i], i))

    return visited

def solution():
    N, M, X = map(int, input().split())
    go = [[100001] * (N+1) for _ in range(N+1)]
    back = [[100001] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        go[i][i] = 0
        back[i][i] = 0
        
    for _ in range(M):
        s, e, c = map(int, input().split())
        go[s][e] = c
        back[e][s] = c

    gom = dijkstra(X, go, N)
    backm = dijkstra(X, back, N)
    maxv= 0
    for i in range(N+1):
        if gom[i] != 100001 and backm[i] != 100001:
            maxv = max(maxv, gom[i] + backm[i])
    print(maxv)


if __name__ == "__main__":
    solution()