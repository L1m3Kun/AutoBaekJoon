import sys
# "".join(<iterable>)  연습 2
# 중복을 제거한 상태로 문자들을 리스트 형식으로 저장(set() 활용)
str_list = list(set(sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline()))))
# 길이와 사전순으로 정렬
str_list.sort(key=lambda x: (len(x),x))
print("\n".join([word for word in str_list]))
