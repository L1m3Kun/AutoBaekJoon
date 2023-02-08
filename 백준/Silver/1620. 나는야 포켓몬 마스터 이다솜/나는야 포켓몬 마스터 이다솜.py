import sys


N, M = map(int, sys.stdin.readline().strip().split())
poke_dictionary = {str(i+1) : sys.stdin.readline().strip() for i in range(N)}
poke_dictionary2 = {val: idx for idx, val in poke_dictionary.items()}
# quest = [sys.stdin.readline().strip() for _ in range(M)]

for i in range(M):
    quest = sys.stdin.readline().strip()
    if poke_dictionary.get(quest) != None:
        print(poke_dictionary.get(quest))
    else:
        print(poke_dictionary2.get(quest))