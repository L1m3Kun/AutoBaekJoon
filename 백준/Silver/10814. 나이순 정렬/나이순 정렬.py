import sys
# "".join(<iterable>) 연습 3
# 튜플로 나이와 이름을 순서와 함께 저장
member = [tuple(sys.stdin.readline().strip().split() + [_] ) for _ in range(int(sys.stdin.readline()))]
# 나이순으로 정렬, 나이가 같으면 입력순으로 정렬
member.sort(key= lambda x: (int(x[0]), int(x[2])))

# join()을 이용하여 출력
print("\n".join([(str(person[0]) + " " + str(person[1])) for person in member]))


''' 오류: 리스트 정렬시 빈 리스트로 만든 후 내용을 복사하고 넣는 방식으로 예상 따라서 리스트 내부 요소를 찾을 수 없음
member = [tuple(sys.stdin.readline().strip().split()) for _ in range(int(sys.stdin.readline()))]
print(member.index(('21', 'Junkyu')))
# 나이순으로 정렬, 나이가 같으면 입력순으로 정렬
member.sort(key= lambda x: (x[0], member.index(x)))

# join()을 이용하여 출력
print("\n".join([(str(person[0]) + " " + str(person[1])) for person in member]))
'''