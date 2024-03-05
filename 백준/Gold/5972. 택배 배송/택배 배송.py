# 5972 택배 배송
import sys, heapq

# dijkstra 구현
input = sys.stdin.readline


def solution():
    # input
    N, M = map(int, input().split())
    # define
    graph = [[] for _ in range(N + 1)]
    # input & graph setting
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    # 방문처리용 list
    visited = [0] * (N + 1)

    que = []

    for node, w in graph[1]:
        heapq.heappush(que, (w, node))

    while que:
        cost, current = heapq.heappop(que)
        if current == N:
            print(cost)
            return
        if visited[current]:
            continue
        visited[current] = 1
        for next, w in graph[current]:
            if visited[next]:
                continue
            heapq.heappush(que, (cost + w, next))


if __name__ == "__main__":
    solution()