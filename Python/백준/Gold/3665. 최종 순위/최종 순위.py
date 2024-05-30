# 3665 최종 순위
import sys
from collections import deque
input = sys.stdin.readline

def main():
    N = int(input())
    ref = tuple(map(int, input().split()))
    rank = [set() for _ in range(N+1)]
    visited = [0] * (N+1)
    # 나보다 순위가 낮은 팀들을 저장
    for i in range(N):
        for j in range(i+1, N):
            rank[ref[i]].add(ref[j])
            visited[ref[j]] += 1
    # print(visited)
    # print(rank)
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if a in rank[b]:
            rank[b].remove(a)
            rank[a].add(b)
            visited[b] += 1
            visited[a] -= 1
        else:
            rank[b].add(a)
            rank[a].remove(b)
            visited[b] -= 1
            visited[a] += 1
    
        # print(visited)
        # print(rank)

    que = deque()
    for i in range(1, N+1):
        if not visited[i]:
            que.append(i)
    
    # print(que)

    if len(que) > 1:
        print("?")
        return
    ans = []

    while que:
        spot = que.popleft()
        ans.append(spot)
        # print(spot, que, ans)
        # print(visited)
        for node in tuple(rank[spot]):
            visited[node] -= 1
            if not visited[node]:
                que.append(node)

    if len(ans) == N:
        print(*ans)
    else:
        print("IMPOSSIBLE")
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        main()