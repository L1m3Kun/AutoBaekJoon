# 22233 가희와 키워드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
keyword = set(input().strip() for _ in range(N))
post = list(list(input().strip().split(',')) for _ in range(M))

for i in range(M):
    for j in post[i]:
        keyword.discard(j)
    
    print(len(keyword))