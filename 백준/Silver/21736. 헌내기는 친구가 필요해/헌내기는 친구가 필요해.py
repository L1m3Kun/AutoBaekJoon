# 21736 헌내기는 친구가 필요해
import sys
from collections import deque
input = sys.stdin.readline


def find_start(N:int, M:int, school:list) -> tuple:
    for i in range(N):
        for j in range(M):
            if school[i][j] == "I":
                return (i, j)
    


def bfs(start:tuple, N:int, M:int, school:list) -> int:
    que = deque([start])
    cnt = 0
    visited = [[0] *M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    while que:
        i, j = que.popleft()
        for di, dj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and school[ni][nj] != "X":
                visited[ni][nj] = 1
                if school[ni][nj] == "P":
                    cnt += 1
                que.append((ni, nj))
    
    return cnt
                




def solution():
    N, M = map(int, input().split())
    school = [input().strip() for _ in range(N)]
    start = find_start(N, M, school)
    ans = bfs(start, N, M, school)
    if ans:
        print(ans)
    else:
        print("TT")

if __name__ == "__main__":
    solution()