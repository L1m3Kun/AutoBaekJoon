# 18110 solved.ac
import sys
input = sys.stdin.readline


def solution(n:int, diffs:list) -> int:
    if n == 0:    return 0
    # 절사 멤버수( = 30%이므로 위, 아래 15% 절사)
    eraze = int(n*0.15 + 0.5)

    # 점수별 정렬
    diffs.sort()
    # 절사 평균 (= 절삭 멤버를 제외한 사람들의 점수의 평균)을 반올림(0.5를 더하면 반올림과 같음)
    return int(sum(diffs[eraze:n-eraze]) / (n-2*eraze) + 0.5)


if __name__ == "__main__":
    # input
    n = int(input())
    diffs = [int(input()) for _ in range(n)]
    # output
    ans = solution(n, diffs)
    print(ans)