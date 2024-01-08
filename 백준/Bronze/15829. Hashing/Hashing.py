# 15829 Hashing
import sys
input = sys.stdin.readline


def hashing(L:int, S:str) -> int:
    hash = 0
    for i in range(L):
        s = S[i]
        a = ord(s)-96
        hash += (a)*(31**i)
    return hash%1234567891

if __name__ == "__main__":
    L = int(input())
    S = input().strip()
    ans = hashing(L,S)
    print(ans)