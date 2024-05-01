# 17070 파이프 옮기기 1
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    home = [list(map(int, input().split())) for _ in range(N)]
    # [가로, 세로, 대각선]
    dp = [[[0,0,0] for _ in range(N-1)] for _ in range(N)]
    # [print(dp[o]) for o in range(N)]
    # print()
    dp[0][0][0] = 1
    for i in range(2, N):
        if not home[0][i]:
            dp[0][i-1][0] += dp[0][i-2][0]
    for i in range(1, N):
        for j in range(2, N):
            if not home[i][j]:
                dp[i][j-1][0] += dp[i][j-2][0] + dp[i][j-2][2]
                dp[i][j-1][1] += dp[i-1][j-1][1] + dp[i-1][j-1][2]
            if not (home[i][j] or home[i-1][j] or home[i][j-1]):
                dp[i][j-1][2] += sum(dp[i-1][j-2])
    # [print(dp[o]) for o in range(N)]
    print(sum(dp[-1][-1]))
            
    return


if __name__ == "__main__":
    main()