import sys
from collections import deque
input = sys.stdin.readline

direction = [(1,0), (0,1), (-1,0), (0,-1)]  # 방향

N, M = map(int, input().strip().split())
maze = [[0] * (M+2)] + [[0] + list(map(int,input().strip())) + [0] for _ in range(N)] +[[0] * (M+2)]
queue = deque([(1,1)])
visited = [[0]*(M+2) for _ in range(N+2)]

visited[1][1] = 1
min_cnt = N*M
while queue:
    i, j = queue.popleft()
    if i == N and j == M:
        if min_cnt > visited[i][j]:
            min_cnt = visited[i][j]
        continue
    elif visited[i][j] > min_cnt:
        continue
    else:
        for di, dj in direction:
            ni = i + di
            nj = j + dj
            if maze[ni][nj] and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

print(min_cnt)