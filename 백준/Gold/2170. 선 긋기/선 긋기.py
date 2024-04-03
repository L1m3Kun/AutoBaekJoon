import sys
input = sys.stdin.readline


def main():
    N = int(input())
    lines = sorted(list(tuple(map(int, input().split())) for _ in range(N)), key = lambda x:x[0])
    start, end = -1000000001,-1000000001
    l = 0
    for s,e in lines:
        if e < start or s > end:
            l += end - start
            start = s
            end = e
        else:
            start = min(start, s)
            end = max(end, e)
    else:
        l+= end-start
    print(l)

if __name__ == "__main__":
    main()