import sys
import heapq
input = sys.stdin.readline

queue = []
N = int(input())
for _ in range(N):
    num = int(input())
    heapq.heappush(queue, num) if num else print(heapq.heappop(queue)) if queue else print(0)