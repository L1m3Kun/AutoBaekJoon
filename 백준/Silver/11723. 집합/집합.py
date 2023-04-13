#11723 집합
import sys
input = sys.stdin.readline

def add(x):
    S.add(x)

def remove(x):
    S.discard(x)

def check(x):
    if x in S:
        return 1
    else:
        return 0

def toggle(x):
    if x in S:
        remove(x)
    else:
        add(x)

    

M = int(input())
S = set()

for _ in range(M):
    order= list(input().strip().split())
    if order[0] == 'add':
        add(int(order[1]))
    elif order[0] == 'remove':
        remove(int(order[1]))
    elif order[0] == 'check':
        print(check(int(order[1])))
    elif order[0] == 'toggle':
        toggle(int(order[1]))
    elif order[0] == 'all':
        S = set(i for i in range(1,21))
    elif order[0] == 'empty':
        S = set()