# 13334 철로
import sys, heapq
input = sys.stdin.readline


def main():
    N = int(input())
    rails = sorted(list(sorted(list(map(int, input().split()))) for _ in range(N)), key=lambda x:(x[1],x[0]))
    d = int(input())
    start, end = -100000001, -100000001
    maxv = 0
    indexes = []
    for s, e in rails:
        if e - s > d:
            continue
        
        if not (start <= s and e <= end):
            maxv = max(maxv, len(indexes))
            start = e-d
            end = e
            while indexes:
                if indexes[0][0] >= start:
                    break
                else:
                    heapq.heappop(indexes)
        heapq.heappush(indexes, (s,e))
    else:
        maxv = max(maxv, len(indexes))
    print(maxv)
    return


if __name__ == "__main__":
    main()
