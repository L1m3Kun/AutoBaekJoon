# 1912 구간 합 구하기 4
import sys
input = sys.stdin.readline


def solution(N:int, M:int, prefix:list) -> int:
    prefix_sum = [0] *N
    prefix_sum[0] = prefix[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i-1] + prefix[i]
    for _ in range(M):
        i, j = map(int, input().split())
        if i == 1:
            print(prefix_sum[j-1])
        else:
            print(prefix_sum[j-1]- prefix_sum[i-2])

    return


if __name__ == "__main__":
    N, M = map(int, input().split())
    prefix = list(map(int, input().strip().split()))
    solution(N, M, prefix)