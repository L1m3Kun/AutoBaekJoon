# 1931 회의실 배정
import sys
from collections import deque
input = sys.stdin.readline

def solution(N:int, meetings:list) -> int:
    meetings.sort(key=lambda x:(x[1], x[0]))
    end = meetings[0][1]
    cnt = 1
    for i in range(1, N):
        s, e = meetings[i]
        if s >= end:
            cnt += 1
            end = e
        
    return cnt


if __name__ == "__main__":
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]
    print(solution(N, meetings))