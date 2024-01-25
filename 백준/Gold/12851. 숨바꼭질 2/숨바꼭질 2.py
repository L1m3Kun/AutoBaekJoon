# 12851 숨바꼭질 2
import sys
from collections import deque
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    que = deque([(0, N)])
    visited = [100000] * 100_001
    visited[N] = 0
    minv = 100_001
    c = 0
    while que:
        cnt, now = que.popleft()
        if now == K:
            if minv > cnt:
                minv = cnt
                c = 1
            elif minv == cnt:
                c += 1
        for next in [now+1, now-1, now<<1]:
            if 0 <= next <=100_000 and visited[next] >= visited[now]+1:
                visited[next] = visited[now] +1
                que.append((cnt+1, next))
    print(minv)
    print(c)

if __name__ == "__main__":
    solution()