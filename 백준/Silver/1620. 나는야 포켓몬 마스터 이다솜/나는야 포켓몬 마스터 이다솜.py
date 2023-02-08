import sys

N, M = map(int, sys.stdin.readline().strip().split())
poke_dictionary = {str(i+1) : sys.stdin.readline().strip() for i in range(N)}
# key값과 val값을 바꿔 dict2생성
poke_dictionary2 = {val: idx for idx, val in poke_dictionary.items()}

# 입력과 동시에 출력
for i in range(M):
    # .strip() 을 안 하면 \n이 같이 입력되어 인덱싱 불가능
    # quest에 입력을 받아 딕셔너리 key에 맞는지 확인
    # 있으면 출력, 없으면 도감을 바꿔서 출력
    quest = sys.stdin.readline().strip()
    # if poke_dictionary.get(quest) != None:
    #     print(poke_dictionary.get(quest))
    # else:
    #     print(poke_dictionary2.get(quest))

    if quest.isalpha():
        print(poke_dictionary2[quest])
    else:
        print(poke_dictionary[quest])
