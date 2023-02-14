import sys

N = int(sys.stdin.readline())
s_list = [sys.stdin.readline().strip() for _ in range(N)]

count = 0

# flag = True
for s in s_list:
    stack = set()
    i = 0
    flag = True
    while i < len(s):
        if s[i] not in stack:
            stack.add(s[i])
            i += 1
            if i<len(s) and s[i] == s[i-1]:
                for j in range(i, len(s)):
                    if s[j] != s[j-1]:
                        break
                    else:
                        i += 1
        else:
            flag = False
            break
    if flag:
        count += 1
print(count)