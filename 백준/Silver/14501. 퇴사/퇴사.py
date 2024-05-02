# 14501 퇴사
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    dp = [0] *(N+2)
    for i in range(1,N+1):
        t, p = map(int, input().split())
        dp[i] = max(dp[i],dp[i-1])
        if i+t <= N+1:
            dp[i+t] = max(dp[i+t],p + dp[i])
        
    else:
        dp[-1] = max(dp[-1], dp[-2])
    print(dp[-1])

    return


if __name__ == "__main__":
    main()