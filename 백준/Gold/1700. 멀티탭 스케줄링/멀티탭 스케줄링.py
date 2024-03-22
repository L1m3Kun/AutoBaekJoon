import sys
input = sys.stdin.readline

def solution(n, k, arr):
    plug = [0] * n      # 멀티탭
    cnt = 0             # 교체 횟수
    idx = 0             # 인덱스
    if n == 1:          # 멀티탭이 1구이면 바로 옆이 같은 경우 말고는 카운트
        for i in range(1, k):
            if arr[i] != arr[i-1]:
                cnt +=1
        return cnt
    # 멀티탭이 2구 이상일 때
    for i in range(k):
        if not arr[i] in plug:
            if idx == n:
                need = [0] * n
                for j in range(n):
                    for l in range(i+1, k):
                        if plug[j] == arr[l]:
                            need[j] = l
                            break
                if 0 in need:
                    plug[need.index(0)] = arr[i]
                    cnt += 1
                else:
                    plug[need.index(max(need))] = arr[i]
                    cnt += 1
                
            else:
                plug[idx] = arr[i]
                idx += 1
    return cnt

N, K = map(int, input().strip().split())
request = list(map(int, input().strip().split()))
print(solution(N, K, request))