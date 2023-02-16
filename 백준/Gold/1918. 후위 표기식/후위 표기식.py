import sys

arr = sys.stdin.readline().strip()

s = ''
oper = []
incom_priority = {'*':2, '/':2, '+':1, '-':1, '(':3}
insta_priority = {'*':2, '/':2, '+':1, '-':1, '(':0}

for i in arr:
    if i not in insta_priority.keys() and i != ')':
        s += i
    elif i == ')':
        if oper:
            for j in range(len(oper)-1,-1,-1):
                if oper[j] == '(':
                    oper.pop()
                    break
                s += oper.pop()
    else:
        if oper:
            for j in range(len(oper)-1, -1, -1):
                if incom_priority[i] <= insta_priority[oper[-1]]:
                    s += oper.pop()
            oper.append(i)

        else:
            oper.append(i)
if oper:
    for k in range(len(oper)-1,-1,-1):
        if oper[k] != '(':
            s += oper.pop()
        else:
            oper.pop()
print(s)