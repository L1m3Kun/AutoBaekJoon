import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x].append(y)
    arr[y].append(x)

queue = deque([1])
visited = [0] * (N+1)
visited[1] = 1
while queue:
    i = queue.popleft()
    for j in arr[i]:
        if not visited[j]:
            visited[j] = i
            queue.append(j)
print(*visited[2:], sep='\n')