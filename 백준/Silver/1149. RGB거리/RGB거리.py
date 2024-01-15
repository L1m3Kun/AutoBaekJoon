# 1149 RGB거리
import sys
input = sys.stdin.readline


def solution(N:int, costs:list) -> int:
    dp = [[1000 * 1000+1] * 3 for _ in range(N)]
    for i in range(3):
        dp[0][i] = costs[0][i]
    for i in range(1, N):
        dp[i][0] = min(dp[i][0], dp[i-1][1]+costs[i][0], dp[i-1][2]+costs[i][0])
        dp[i][1] = min(dp[i][1], dp[i-1][0]+costs[i][1], dp[i-1][2]+costs[i][1])
        dp[i][2] = min(dp[i][2], dp[i-1][0]+costs[i][2], dp[i-1][1]+costs[i][2])
    return min(dp[-1])


if __name__ == "__main__":
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, costs))