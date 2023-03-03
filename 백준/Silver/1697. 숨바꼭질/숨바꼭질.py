import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
queue = deque([N])
min_cnt = abs(K-N)
visited = [0] * (10**5+1)
if N == K:
    print(0)
else:
    while queue:
        now = queue.popleft()
        if now == K:
            min_cnt = min(min_cnt, visited[now])
        elif visited[now] > min_cnt:
            pass
        else:
            # if now > K:
            if now -1 >= 0 and not visited[now-1]:
                queue.append(now-1)
                visited[now-1] = visited[now] + 1
            # else:
            if now + 1 <= 100000 and not visited[now+1]:
                queue.append(now+1)
                visited[now+1] = visited[now] + 1
            if (now <<1) <= 100000 and not visited[now<<1]:
                queue.append(now<<1)
                visited[now<<1] = visited[now] + 1
    print(min_cnt)