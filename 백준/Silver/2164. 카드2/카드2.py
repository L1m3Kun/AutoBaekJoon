import sys
from collections import deque
# 입력받은 N으로 1부터 N까지 덱 생성
card_list = deque(range(1,int(sys.stdin.readline())+1))
# 제일 위에 한장 버리고 한장 내리고를 1장이 남을때까지 반복
while len(card_list) != 1:
    card_list.popleft()
    card_list.append(card_list.popleft())
# 마지막 1장 출력
print(*card_list)