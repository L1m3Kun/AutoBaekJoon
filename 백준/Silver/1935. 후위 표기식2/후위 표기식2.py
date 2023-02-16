import sys

def calculate(st, dic):
    num = []
    for s in st:
        if s.isalpha():
            num.append(dic[s])
        else:
            if len(num) >= 2:
                a = num.pop()
                b = num.pop()
                if s == '*':
                    num.append(a*b)
                elif s == '+':
                    num.append(a+b)
                elif s == '-':
                    num.append(b-a)
                elif s == '/':
                    num.append(b/a)
            else:
                return
    if len(num) == 1:
        return num.pop()
    else:
        return


N = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip()
str_dic = {}
for i in range(65, 65+N):
    str_dic[chr(i)] = int(sys.stdin.readline().strip())

print('%.2f' %calculate(arr,str_dic))

# print(ord('A')) # 65

