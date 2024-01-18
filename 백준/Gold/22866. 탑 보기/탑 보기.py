# 22866 탑보기
import sys
input = sys.stdin.readline


def solution(N:int, L:list) -> list:
    dp = [[0,N*N]] * N #(cnt, nearest)
    left = [0]
    for i in range(1,N):
        if not left or  L[i] < L[left[-1]]:
            dp[i] = [len(left), left[-1] if left else N*N]
            left.append(i)
        else:
            j = len(left)-1
            while True:
                if not left or L[left[j]] > L[i]:
                    if left:
                        dp[i] = [len(left), left[-1]]
                    else:
                        dp[i] = [len(left), N*N]

                    left.append(i)
                    break
                left.pop()
                j -= 1
    right = [N-1]
    for i in range(N-2, -1, -1):
        if not right or L[i] < L[right[-1]]:
            dp[i][0] += len(right)
            if right and abs(right[-1] - i) < abs(i-dp[i][1]):
                dp[i][1] = right[-1]


            right.append(i)
        else:
            j = len(right)-1
            while True:
                if not right or L[right[j]] > L[i]:
                    dp[i][0] += len(right)
                    if right and abs(right[-1] - i) < abs(i-dp[i][1]):
                        dp[i][1] = right[-1]
                    right.append(i)
                    break
                right.pop()
                j -= 1
    return dp


if __name__ == "__main__":
    N = int(input())
    ans = solution(N, list(map(int, input().split())))
    for i in range(N):
        if ans[i][0]!= 0:
            print(ans[i][0], ans[i][1]+1)
        else:
            print(0)
