N, M = map(int, input().split())
arr_A = []
arr_B = []
# 행렬 입력
for idx in range(N): 
    arr_A.append(list(map(int,input().split())))
for idx in range(N):
    arr_B.append(list(map(int,input().split())))
total = []
for n in range(N):
    for m in range(M):
        print(arr_A[n][m] + arr_B[n][m], end = ' ')
    print("")
