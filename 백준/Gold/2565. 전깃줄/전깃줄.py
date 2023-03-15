import sys
input = sys.stdin.readline

N = int(input())
inc = [1] * N
# dec = [1] * N
line = {}
for i in range(N):
    idx, node = map(int, input().split())
    line[idx] = node
line_list = sorted(list(line.keys()))
arr = [line[i] for i in line_list]
# rev_arr = arr[::-1]
max_val = 0
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        # if rev_arr[i] > rev_arr[j]:
        #     dec[i] = max(dec[i], dec[j] + 1)
    max_val = max(max_val, inc[i])
print(N-max_val)
