import sys

# 문자열 입력 저장
N = sys.stdin.readline()

# 문자열 리스트로 바꾼 후 내림차순 정렬
n_lst = list(N)
n_lst.sort(reverse=1)

#문자열 합치기
result = ''
for num in n_lst:
    result += num
print(result)