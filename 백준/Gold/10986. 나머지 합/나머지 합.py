# 10986 나머지 합
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    presum = [0] * (N+1)
    remain = defaultdict(int)
    
    
    for i in range(1, N+1):
        presum[i] = (arr[i-1] + presum[i-1]) % M
        remain[presum[i]] += 1
    
    ans = remain[0]

    for cnt in remain.values():
        
        ans += cnt * (cnt-1) // 2
        
    print(ans)



if __name__ =="__main__":
    main()
