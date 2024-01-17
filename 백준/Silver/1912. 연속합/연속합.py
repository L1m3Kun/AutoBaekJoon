import sys
input = sys.stdin.readline


def solution(N:int, arr:list) -> int:
    for i in range(1, N):
        arr[i] = max(arr[i], arr[i] +arr[i-1])
    return max(arr)

# def solution(N:int, arr:list) -> int:
#     # i 번째 인덱스 까지 누적합을 구하기
#     # i 번째 인덱스 까지 누적합 중 가장 작은 값을 저장하는 배열 생성
#     # i 번째 누적합에서 i-1번째까지 누적합 중 최솟값을 빼면 최장 수열
#     small = [0] * N
#     small[0] = arr[0]
#     for i in range(1, N):
#         arr[i] += arr[i-1]
#         small[i] = min(small[i-1], arr[i])        
#     ans = max(arr)
#     for i in range(N-1,0,-1):
#         ans = max(ans, arr[i] - small[i-1])
        
#     return ans


if __name__ == "__main__":
    print(solution(int(input()), list(map(int, input().split()))))