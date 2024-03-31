# 2467 용액
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    liquid = sorted(tuple(map(int, input().split())))

    i, j = 0, N-1
    minv = 2_000_000_001
    ans = (-1, -1)
    while i < j:
        mid = liquid[i] + liquid[j]

        if abs(minv) > abs(mid):
            minv = mid
            ans = (liquid[i], liquid[j])

        if mid == 0:
            ans = (liquid[i], liquid[j])
            break
        elif mid < 0:
            i += 1
        else:
            j -= 1
    print(*ans)


if __name__ == "__main__":
    main()