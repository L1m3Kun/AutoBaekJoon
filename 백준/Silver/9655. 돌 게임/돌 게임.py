import sys
input = sys.stdin.readline

N = int(input())
print("SK") if (N//3 + N%3)%2 else print("CY")