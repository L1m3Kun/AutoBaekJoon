# 2470 두 용액
import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    s,e = 0, N-1
    pair = tuple()
    minv = 1_000_000_001*N
    while s<e:
        if minv > abs(arr[s] + arr[e]):
            minv = abs(arr[s] + arr[e])
            pair = tuple([arr[s], arr[e]])
            
        if arr[s] + arr[e] < 0:
            s += 1
        elif arr[s] + arr[e] > 0:
            e -= 1
        else:
            break

    print(*pair)

if __name__ == "__main__":
    solution()