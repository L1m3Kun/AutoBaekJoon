# 10655 마라톤 1
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    checkPoints = [tuple(map(int, input().split())) for _ in range(N)]

    def distance(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    
    total = 0
    maxDiffer = -1000000
    for idx in range(1,N-1):
        (previ,prevj), (i,j), (posti,postj) = checkPoints[idx-1], checkPoints[idx], checkPoints[idx+1]
        nonSkip = [distance(previ,prevj,i,j), distance(i,j,posti,postj)]
        skipped = distance(previ,prevj,posti,postj)
        differ = sum(nonSkip) - skipped
        total += nonSkip[0]
        maxDiffer = max(differ, maxDiffer)
    else:
        total += nonSkip[1]

    print(total - maxDiffer)    
    
    return


if __name__ == "__main__":
    main()