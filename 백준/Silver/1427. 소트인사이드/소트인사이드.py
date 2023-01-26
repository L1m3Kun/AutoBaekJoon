import sys

N = sys.stdin.readline()
n_lst = list(N)
n_lst.sort(reverse=1)
result = ''
for num in n_lst:
    result += num
print(result)