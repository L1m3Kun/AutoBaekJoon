import sys
input = sys.stdin.readline

def ispalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-1-i]:
            return 0
    return 1

s = input().strip()
maxV = -1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        maxV= 0
        break
if maxV == 0:
    for j in range(len(s), -1, -1):
        if not ispalindrome(s[:j]):
            maxV = len(s[:j])
            break
print(maxV)    