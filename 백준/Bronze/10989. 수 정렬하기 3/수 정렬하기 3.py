import sys
# count 정렬 활용하기
N = int(sys.stdin.readline())
num_list = [0] * 10001
for _ in range(N):
    num=int(sys.stdin.readline())
    num_list[num] += 1
for idx in range(len(num_list)):
    if num_list[idx] != 0:
        for _ in range(num_list[idx]):
            print(idx)