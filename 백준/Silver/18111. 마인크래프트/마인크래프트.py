# 18111 마인크래프트
import sys
from collections import defaultdict
input = sys.stdin.readline


def check(candidate:defaultdict, h:int):
    mine, build = 0, 0
    for key, val in candidate.items():
        key = int(key)
        if key != h:
            diff = abs(key - h) * val
            if key > h:
                mine += diff 
            else:
                build += diff 
    return -1 if mine+B <build else 2*mine+build


def solution():
    min_t,ans =1e9,-1
    for h in range(minh, maxh+1):
        time = check(house, h)
        if time >= 0:
            if min_t > time:
                min_t = time
                ans = h
            elif min_t == time:
                if ans < h:
                    ans = h
    return (min_t, ans)


if __name__ == "__main__":
    N, M, B = map(int, input().split())
    house = defaultdict(int)
    minh,maxh = 257, -1
    for _ in range(N):
        for j in list(map(int, input().split())):
            house[j] += 1            
            minh = min(minh, j)       
            maxh = max(maxh, j)       
    print(*solution())