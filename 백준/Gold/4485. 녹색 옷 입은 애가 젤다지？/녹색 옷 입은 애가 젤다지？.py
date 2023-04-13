# 4485 녹색 옷 입은 애가 젤다지?
import sys
from collections import deque
import heapq
input = sys.stdin.readline

T = 0
dir = [(0,1),(0,-1),(1,0),(-1,0)]   # 젤ㄷ..아니 링크 방향
INF = 10 * 125*125
while True:
    T += 1 # test case
    N = int(input())
    if not N:   # N이 0이면 멈춰!
        break
    cave = [list(map(int, input().strip().split())) for _ in range(N)]  # 도둑놈들
    que = []
    heapq.heappush(que,(cave[0][0],0,0))
    visited = [[INF] * N for _ in range(N)]
    while que:
        w, i, j = heapq.heappop(que)
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] > w+cave[ni][nj]:
                    heapq.heappush(que, (w+cave[ni][nj], ni, nj))
                    visited[ni][nj] = w+cave[ni][nj]


    print(f'Problem {T}: {visited[-1][-1]}')