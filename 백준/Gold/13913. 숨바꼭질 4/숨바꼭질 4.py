# 13913 숨바꼭질 4
import sys
from collections import deque
input = sys.stdin.readline


def solution():
    N, K = map(int,input().split())
    que = deque([(0, N)])
    limit = 100_001

    # visited 배열을 통해 내가 지나온 길 표시 now -> next
    visited= [-1] * limit
    visited[N] = N
    minv = limit
    ans = []
    while que:
        cost, now = que.popleft()
        if now == K:
            minv = min(minv, cost)
            prev = K
            while prev != N:
                ans.append(prev)
                prev = visited[prev]
            ans.append(N)
            
            break
        for next in [now+1, now-1, now*2]:
            if 0 <= next < limit and visited[next] == -1:
                visited[next] = now
                que.append((cost+1, next))
                
    print(minv)
    print(*ans[::-1])
    

    return


if __name__ == "__main__":
    solution()  