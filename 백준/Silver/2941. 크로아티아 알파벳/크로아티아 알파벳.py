import sys

s = sys.stdin.readline().strip()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
i = 0
while i < len(s):
    for j in range(1,3):
        if s[i:i+j+1] in cro_alpha:
            count += j
            i += j
            break
    i += 1
print(len(s) - count)