import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
ladder = {}
for _ in range(N+M):
    spot, node = map(int, input().strip().split())
    ladder[spot] = node

queue = deque([1])
visited = [0,1] + [0] * 99
while queue:
    start = queue.popleft()
    if start == 100:
        break
    for go in range(1, 7):
        idx = start + go
        if idx in ladder.keys():
            idx = ladder[idx]
        if idx <= 100 and not visited[idx]:
            visited[idx] = visited[start] + 1
            queue.append(idx)
print(visited[100]-1)