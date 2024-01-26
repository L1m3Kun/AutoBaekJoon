# 13549 숨바꼭질 3
import sys, heapq
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    que = []
    limit = 100_001
    heapq.heappush(que, (0, N))
    visited = [0] * limit
    visited[N] = 0
    min_v = limit
    while que:
        cost, now = heapq.heappop(que)
        if now == K:
            min_v = min(min_v, cost)
        for next in [now-1, now+1, now*2]:
            if 0 <= next < limit and not visited[next]:
                if next == now * 2:
                    heapq.heappush(que, (cost, next))
                    visited[next] = 1
                else:
                    heapq.heappush(que, (cost+1, next))
                    visited[next] = 1
    print(min_v)
    
    return


if __name__ == "__main__":
    solution()