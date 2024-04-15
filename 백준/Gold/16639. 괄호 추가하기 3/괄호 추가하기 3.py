# 16639 괄호 추가하기 3
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    nums = []
    operator = []
    for s in list(input().strip()):
        if s.isdecimal():
            nums.append(int(s))
        else:
            operator.append(s)
    maxn = N // 2 + 1
    dp = [[[0,0] for _ in range((maxn))] for _ in range(maxn)]


    def get_value(oper,  start, pin, end):
        arr = [
            calculate(oper[pin], dp[start][pin][0], dp[pin+1][end][0]),
            calculate(oper[pin], dp[start][pin][0], dp[pin+1][end][1]),
            calculate(oper[pin], dp[start][pin][1], dp[pin+1][end][0]),
            calculate(oper[pin], dp[start][pin][1], dp[pin+1][end][1])
        ]
        return (max(arr), min(arr))


    def calculate(operator, num1, num2):
        if operator == "*":
            return num1 * num2
        elif operator == "+":
            return num1 + num2
        else:
            return num1 - num2

    # [print(*dp[i]) for i in range(maxn)]

    for cnt in range(maxn):
        for i in range(maxn-cnt):
            j = i + cnt
    
            if cnt:
                dp[i][j] = [-9**maxn,9**maxn]
                for p in range(i,j):
                    maxv, minv = get_value(operator, i, p, j)
                    dp[i][j] = [max(maxv, dp[i][j][0]), min(minv, dp[i][j][1])]
            else:
                dp[i][j] = [nums[i], nums[i]]
            
    # [print(*dp[i]) for i in range(maxn)]
    print(dp[0][-1][0])
    


if __name__ == "__main__":
    main()
