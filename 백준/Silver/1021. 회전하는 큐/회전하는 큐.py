import sys

N, M = map(int, sys.stdin.readline().strip().split())
N_list = list(range(1,N+1))
M_list = list(map(int, sys.stdin.readline().strip().split()))
count = 0
# 뽑아낼 리스트가 비워지면 끝
while M_list:
    # N_list 여부 확인
    if N_list:
        # 맨앞에 있으면 바로 뽑아냄
        if N_list[0] == M_list[0]:
            N_list.pop(0)
            M_list.pop(0)
        else:
        # 앞에 없으면 인덱스 비교해서 앞이랑 뒤 중에 가까운 쪽으로 움직임
            if N_list.index(M_list[0]) > len(N_list)//2:
                # >>
                arr = [N_list.pop()] + N_list
                N_list = arr.copy()
                count += 1
            else:
                # <<
                N_list.append(N_list.pop(0))
                count += 1
    else:
        # 무한루프 방지
        break
print(count)