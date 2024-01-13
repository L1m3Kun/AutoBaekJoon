# 11279 최대힙
import sys, heapq
input = sys.stdin.readline


def solution(N:int):
    que = []
    for _ in range(N):
        x = int(input())
        if x:
            heapq.heappush(que, -x)
        else:
            if que:
                print(-heapq.heappop(que))
            else:
                print(0)

    return


if __name__ == "__main__":
    N = int(input())
    solution(N)