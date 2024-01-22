# 7785 회사에 있는 사람
import sys
input = sys.stdin.readline


def solution(N:int):
    company = set()
    for _ in range(N):
        person, order = input().strip().split()
        if order == "enter":
            company.add(person)
        else:
            company.discard(person)    
    return sorted(list(company), reverse=1)

if __name__ == "__main__":
    print(*solution(int(input())), sep= "\n")