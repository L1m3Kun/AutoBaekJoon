N = int(input())
n_lst = []
for _ in range(N):
    n_lst.append(int(input()))      # list 저장
n_lst.sort()                        # 오름차순 정렬
for idx in n_lst:
    print(idx)                      # 출력