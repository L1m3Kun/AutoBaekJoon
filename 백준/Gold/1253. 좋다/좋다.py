import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
if sum(arr):
    hash = {}
    for i in range(N):
      hash[arr[i]] = i
    cnt = 0
    for i in range(N):
        for j in range(N):
          add = arr[i] - arr[j]
          if i!= j and add in hash and hash[add] != i and hash[add] != j:
            cnt += 1
            break
    print(cnt)
else:
    print(N)