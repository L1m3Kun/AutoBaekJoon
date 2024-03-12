# 11399 ATM
import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    for i in range(1, N):
        arr[i] += arr[i-1]
    print(sum(arr))

if __name__ == "__main__":
    solution()