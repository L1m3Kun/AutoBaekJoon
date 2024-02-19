# 16953 A -> B
import sys,heapq
input = sys.stdin.readline



def solution():
    a, b = map(int, input().split())
    limit = b-a+1
    visited = set([a])
    que = []
    heapq.heappush(que, (0, a))
    
    ans = -1
    while que:
        cnt, node = heapq.heappop(que)

        if node == b:
            ans = cnt
            break

        for post in [node*2, node*10+1]:
            if post <= b and post not in visited:
                visited.add(post)
                heapq.heappush(que, (cnt+1, post))

    if ans != -1:
        print(ans+1)
    else:
        print(-1)

if __name__ == "__main__":
    solution()