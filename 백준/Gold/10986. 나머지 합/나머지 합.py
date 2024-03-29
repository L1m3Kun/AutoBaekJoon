# 10986 나머지 합
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    remain = defaultdict(int)
    
    remain[arr[0]%M] += 1
    for i in range(1, N):
        arr[i] = arr[i] + arr[i-1]
        remain[arr[i] % M] += 1
    
    ans = remain[0]

    for cnt in remain.values():
        
        ans += cnt * (cnt-1) // 2
        
    print(ans)



if __name__ =="__main__":
    main()
