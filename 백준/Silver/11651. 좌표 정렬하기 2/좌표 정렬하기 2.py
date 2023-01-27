import sys
# join() 함수 연습
# 사용법:
# "".join(<iterable>) = > [0][1][2]""

# matrix_list 선언 및 초기화
# [for _ in _] 삼항 연산자 -> type(list)
# 리스트(튜플) 형식으로 선언, 처음 입력 받은 수만큼 반복
matrix_list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(int(sys.stdin.readline()))]
# key를 이용한 정렬 기준 변경
matrix_list.sort(key=lambda x: (x[1], x[0]))

#"\n".join( ) <- 마지막에 줄바꿈
# <iterable>: [for] 삼항 연산자로 list형식
# 리스트 원소: matrix_list[<변수>][0] + " " + matrix_list[<변수>][1] 변수를 matrix_list 원소 개수만큼 반복
print("\n".join([(str(x[0])+" "+str(x[1])) for x in matrix_list]))