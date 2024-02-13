# 2559 수열
import sys
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))
    prefix = [0] * N
    prefix[0] = seq[0]
    for i in range(1, N):
        prefix[i] = prefix[i-1] + seq[i]
    
    j = K
    max_value = prefix[K-1]
    while j < N:
        max_value = max(max_value,  prefix[j]-prefix[j-K])
        j += 1
    print(max_value)

if __name__ == "__main__":
    solution()