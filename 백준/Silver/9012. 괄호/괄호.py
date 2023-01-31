import sys

for bracket in range(int(sys.stdin.readline())):
    bracket = list(sys.stdin.readline().strip())
    # stack = [idx for idx in bracket]
    # print(bracket)
    count = 0
    for idx in range(len(bracket)):
        if bracket[idx] == '(':
            count += 1
        elif bracket[idx] == ')':
            count -= 1
        if count < 0:
            print('NO')
            break    
    else:
        if count == 0:
            print('YES')
        else:
            print('NO')