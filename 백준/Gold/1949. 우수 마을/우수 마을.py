# 1949 우수마을
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(now:int) -> None:
    for next in neighbor[now]:
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            dp[now][0] = dp[now][0] + max(dp[next][1], dp[next][0])
            dp[now][1] = dp[now][1] + dp[next][0]
    return


if __name__ == "__main__":
    N = int(input())
    population = [0]+list(map(int, input().split()))
    neighbor = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        neighbor[a].append(b)
        neighbor[b].append(a)
    dp = [[0,population[i]] for i in range(N+1)]
    
    visited = [0] * (N+1)
    visited[1]=1
    dfs(1)
    print(max(dp[1]))
