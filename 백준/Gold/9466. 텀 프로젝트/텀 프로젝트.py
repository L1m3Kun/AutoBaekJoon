import sys
input = sys.stdin.readline

def dfs(i):
    global ans
    cycle = []
    while True:
        cycle.append(i)
        visited[i] = 1
        next = arr[i]
        if visited[next]:
            if next in cycle:
                ans += len(cycle[cycle.index(next):])
            return
        else:
            i = next

for _ in range(int(input())):
    N = int(input())
    # arr = [0] * (N+1)
    # visited = [1]+[0] * N
    # ans = 0
    # for idx, num in enumerate(map(int, input().strip().split())):
    #     if idx + 1 != num:
    #         arr[idx+1] = num
    #     else:
    #         visited[idx+1] = 1
    #         ans += 1
    arr = [0]+list(map(int, input().strip().split()))
    visited = [1] + [0] * N
    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
    print(N - ans)
    