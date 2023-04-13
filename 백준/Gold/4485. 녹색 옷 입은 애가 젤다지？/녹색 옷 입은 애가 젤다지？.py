#4485 녹색 옷 입은 애가 젤다지?
import sys
from collections import deque

input = sys.stdin.readline
T = 0
while True:
    T += 1
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().strip().split())) for _ in range(N)]
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    que = deque([(0,0)])
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = cave[0][0]+1
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N: 
                if not visited[ni][nj]:
                    que.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + cave[ni][nj]
                elif visited[ni][nj] > visited[i][j] + cave[ni][nj]:
                    visited[ni][nj] = visited[i][j] + cave[ni][nj]
                    que.append((ni,nj))
    print(f'Problem {T}: {visited[-1][-1]-1}')
                

