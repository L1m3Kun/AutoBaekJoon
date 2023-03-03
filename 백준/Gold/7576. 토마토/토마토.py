import sys
from collections import deque
input = sys.stdin.readline



M, N = map(int, input().strip().split())
storage = [list(map(int, input().strip().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


queue = deque([])
test = 0
for i in range(N):
    test += sum(storage[i])
    for j in range(M):
        if storage[i][j] == 1:
            queue.append((i,j))
if test == -(N*M):
    print(-1)
else:
    while queue:
        i, j = queue.popleft()
        res = storage[i][j]
        for di, dj in direction:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and storage[ni][nj] == 0:
                storage[ni][nj] = storage[i][j]+1
                queue.append((ni,nj))
# [print(*storage[i]) for i in range(N)]
for i in range(N):
    for j in range(M):
        if storage[i][j] == 0:
            res = 0
print(res-1)