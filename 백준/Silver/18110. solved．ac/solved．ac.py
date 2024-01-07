# 18110 solved.ac
import sys
input = sys.stdin.readline


def solution(n:int, diffs:list) -> int:
    if n == 0:    return 0
    # 절사 멤버수( = 30%이므로 위, 아래 15% 절사)
    eraze = n*0.15
    if eraze - int(eraze) >= 0.5:
        eraze = int(eraze) + 1
    else:
        eraze = int(eraze)

    # 점수별 정렬
    diffs.sort()
    # 절사 평균 (= 절삭 멤버를 제외한 사람들의 점수의 평균)을 반올림
    diff = sum(diffs[eraze:n-eraze]) / (n-2*eraze)
    if diff - int(diff) >= 0.5:
        return int(diff) +1
    else:
        return int(diff)


if __name__ == "__main__":
    # input
    n = int(input())
    diffs = [int(input()) for _ in range(n)]
    # output
    ans = solution(n, diffs)
    print(ans)