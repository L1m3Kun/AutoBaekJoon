# 2607 비슷한 단어
import sys
from collections import defaultdict
input = sys.stdin.readline


def solution(N:int, words:list) -> int:
    cnt = 0
    word = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        for w in words[i]:
            word[i][w] += 1
    for i in range(1, N):
        inw = 0
        absi = 0
        for j in word[0].keys():
            word[i][j] -= word[0][j]
        for j in word[i].values():
            inw += j
            absi += abs(j)
            if absi > 2:
                break
        else:
            if abs(inw) <= 1:
                cnt += 1

    return cnt 



if __name__ == "__main__":
    N = int(input())
    print(solution(N, [input().strip() for _ in range(N)]))
