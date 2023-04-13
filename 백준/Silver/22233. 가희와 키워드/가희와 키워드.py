# 22233 가희와 키워드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
keyword = set(input().strip() for _ in range(N))

for i in range(M):
    for j in list(input().strip().split(',')):
        keyword.discard(j)
    
    print(len(keyword))