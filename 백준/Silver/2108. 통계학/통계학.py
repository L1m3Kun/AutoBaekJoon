import sys

def average(n_lst):
    return round(sum(n_lst)/len(n_lst))

def center(n_lst):
    return sorted(n_lst)[len(n_lst)//2]

def most_counted(n_lst):
    count_dic = {}
    count_list = []
    max = -4000
    for num in n_lst:
        if num not in count_dic.keys():     # dict 저장
            count_dic[num] = 1
        else:
            count_dic[num] += 1
    for val in count_dic.values():      # max 가 최대일때 key값 저장
        if val > max:
            max = val
    for key, val in count_dic.items():
        if max == val:
            count_list.append(key)
    count_list.sort()                       # 정렬
    if len(count_list) != 1:                # 갯수가 2개 이상이면 두번째 값 출력
        return count_list[1]
    else:
        return count_list[0]

def ran_lst(n_lst):
    return sorted(n_lst)[-1] - sorted(n_lst)[0]         # 정렬 후 가장 끝들의 차이

N = int(sys.stdin.readline())
n_list = []
for _ in range(N):
    n_list.append(int(sys.stdin.readline()))

print(average(n_list))
print(center(n_list))
print(most_counted(n_list))
print(ran_lst(n_list))